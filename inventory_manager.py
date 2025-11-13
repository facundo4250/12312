#!/usr/bin/env python3
"""
Sistema de Gestión de Inventario Farmacéutico - Farmacia Nieto
Sistema completo para gestionar productos, stock y vencimientos
@author Código de Ejemplo
@version 1.0.0
"""

from datetime import datetime, timedelta
from typing import List, Dict, Optional
import json
from dataclasses import dataclass, asdict
from enum import Enum


class ProductCategory(Enum):
    """Categorías de productos farmacéuticos"""
    ORTOMOLECULAR = "ortomolecular"
    DERMOCOSMETICA = "dermocosmetica"
    HOMEOPATIA = "homeopatia"
    ALOPATICA = "alopatica"
    FITOTERAPIA = "fitoterapia"
    FLORALES = "florales"
    PROBIOTICOS = "probioticos"
    HORMONAS = "hormonas"
    MATERIA_PRIMA = "materia_prima"
    OTROS = "otros"


@dataclass
class Product:
    """Clase para representar un producto farmacéutico"""
    id: str
    name: str
    category: ProductCategory
    description: str
    stock_quantity: int
    min_stock: int
    unit_price: float
    expiration_date: Optional[datetime] = None
    batch_number: Optional[str] = None
    supplier: Optional[str] = None
    storage_location: Optional[str] = None

    def is_low_stock(self) -> bool:
        """Verifica si el stock está bajo"""
        return self.stock_quantity <= self.min_stock

    def is_expired(self) -> bool:
        """Verifica si el producto está vencido"""
        if not self.expiration_date:
            return False
        return datetime.now() > self.expiration_date

    def days_until_expiration(self) -> Optional[int]:
        """Calcula los días hasta el vencimiento"""
        if not self.expiration_date:
            return None
        delta = self.expiration_date - datetime.now()
        return delta.days

    def is_near_expiration(self, days_threshold: int = 30) -> bool:
        """Verifica si el producto está próximo a vencer"""
        days = self.days_until_expiration()
        if days is None:
            return False
        return 0 < days <= days_threshold

    def to_dict(self) -> Dict:
        """Convierte el producto a diccionario"""
        data = asdict(self)
        data['category'] = self.category.value
        if self.expiration_date:
            data['expiration_date'] = self.expiration_date.isoformat()
        return data


class InventoryManager:
    """Gestor principal del inventario farmacéutico"""

    def __init__(self):
        self.products: Dict[str, Product] = {}
        self.transactions: List[Dict] = []

    def add_product(self, product: Product) -> bool:
        """
        Agrega un nuevo producto al inventario

        Args:
            product: Producto a agregar

        Returns:
            bool: True si se agregó exitosamente
        """
        if product.id in self.products:
            print(f"⚠️  Producto {product.id} ya existe en el inventario")
            return False

        self.products[product.id] = product
        self._log_transaction("ADD", product.id, product.stock_quantity)
        print(f"✅ Producto {product.name} agregado exitosamente")
        return True

    def remove_product(self, product_id: str) -> bool:
        """
        Elimina un producto del inventario

        Args:
            product_id: ID del producto a eliminar

        Returns:
            bool: True si se eliminó exitosamente
        """
        if product_id not in self.products:
            print(f"❌ Producto {product_id} no encontrado")
            return False

        product = self.products[product_id]
        del self.products[product_id]
        self._log_transaction("REMOVE", product_id, 0)
        print(f"🗑️  Producto {product.name} eliminado del inventario")
        return True

    def update_stock(self, product_id: str, quantity_change: int, reason: str = "") -> bool:
        """
        Actualiza el stock de un producto

        Args:
            product_id: ID del producto
            quantity_change: Cambio en la cantidad (positivo para agregar, negativo para restar)
            reason: Razón del cambio

        Returns:
            bool: True si se actualizó exitosamente
        """
        if product_id not in self.products:
            print(f"❌ Producto {product_id} no encontrado")
            return False

        product = self.products[product_id]
        new_quantity = product.stock_quantity + quantity_change

        if new_quantity < 0:
            print(f"❌ No hay suficiente stock. Disponible: {product.stock_quantity}")
            return False

        product.stock_quantity = new_quantity
        self._log_transaction("UPDATE", product_id, quantity_change, reason)

        # Alertas automáticas
        if product.is_low_stock():
            print(f"⚠️  ALERTA: Stock bajo para {product.name}. Cantidad: {product.stock_quantity}")

        print(f"✅ Stock actualizado: {product.name} - Nuevo stock: {product.stock_quantity}")
        return True

    def get_product(self, product_id: str) -> Optional[Product]:
        """Obtiene un producto por su ID"""
        return self.products.get(product_id)

    def search_products(self, query: str) -> List[Product]:
        """
        Busca productos por nombre o descripción

        Args:
            query: Texto a buscar

        Returns:
            Lista de productos que coinciden
        """
        query_lower = query.lower()
        results = [
            product for product in self.products.values()
            if query_lower in product.name.lower() or query_lower in product.description.lower()
        ]
        return results

    def get_products_by_category(self, category: ProductCategory) -> List[Product]:
        """Obtiene todos los productos de una categoría"""
        return [
            product for product in self.products.values()
            if product.category == category
        ]

    def get_low_stock_products(self) -> List[Product]:
        """Obtiene productos con stock bajo"""
        return [
            product for product in self.products.values()
            if product.is_low_stock()
        ]

    def get_expired_products(self) -> List[Product]:
        """Obtiene productos vencidos"""
        return [
            product for product in self.products.values()
            if product.is_expired()
        ]

    def get_near_expiration_products(self, days_threshold: int = 30) -> List[Product]:
        """Obtiene productos próximos a vencer"""
        return [
            product for product in self.products.values()
            if product.is_near_expiration(days_threshold)
        ]

    def generate_stock_report(self) -> str:
        """Genera un reporte del estado del inventario"""
        total_products = len(self.products)
        total_stock = sum(p.stock_quantity for p in self.products.values())
        low_stock = len(self.get_low_stock_products())
        expired = len(self.get_expired_products())
        near_expiration = len(self.get_near_expiration_products())

        report = f"""
╔══════════════════════════════════════════════════════════════╗
║          REPORTE DE INVENTARIO - FARMACIA NIETO              ║
╚══════════════════════════════════════════════════════════════╝

📊 ESTADÍSTICAS GENERALES:
   • Total de productos: {total_products}
   • Unidades totales en stock: {total_stock}
   • Productos con stock bajo: {low_stock}
   • Productos vencidos: {expired}
   • Productos próximos a vencer (30 días): {near_expiration}

🏷️  PRODUCTOS POR CATEGORÍA:
"""
        for category in ProductCategory:
            count = len(self.get_products_by_category(category))
            if count > 0:
                report += f"   • {category.value.title()}: {count} productos\n"

        if low_stock > 0:
            report += "\n⚠️  ALERTAS DE STOCK BAJO:\n"
            for product in self.get_low_stock_products():
                report += f"   • {product.name}: {product.stock_quantity} unidades (mínimo: {product.min_stock})\n"

        if near_expiration > 0:
            report += "\n⏰ PRODUCTOS PRÓXIMOS A VENCER:\n"
            for product in self.get_near_expiration_products():
                days = product.days_until_expiration()
                report += f"   • {product.name}: {days} días\n"

        if expired > 0:
            report += "\n❌ PRODUCTOS VENCIDOS (RETIRAR DEL INVENTARIO):\n"
            for product in self.get_expired_products():
                report += f"   • {product.name} - Lote: {product.batch_number}\n"

        report += "\n" + "═" * 64 + "\n"
        return report

    def _log_transaction(self, action: str, product_id: str, quantity: int, reason: str = ""):
        """Registra una transacción en el historial"""
        transaction = {
            'timestamp': datetime.now().isoformat(),
            'action': action,
            'product_id': product_id,
            'quantity': quantity,
            'reason': reason
        }
        self.transactions.append(transaction)

    def save_to_file(self, filename: str = "inventory.json"):
        """Guarda el inventario en un archivo JSON"""
        data = {
            'products': [product.to_dict() for product in self.products.values()],
            'transactions': self.transactions
        }
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"💾 Inventario guardado en {filename}")

    def load_from_file(self, filename: str = "inventory.json"):
        """Carga el inventario desde un archivo JSON"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                data = json.load(f)

            self.products = {}
            for product_data in data.get('products', []):
                # Convertir categoría de string a enum
                product_data['category'] = ProductCategory(product_data['category'])
                # Convertir fecha de string a datetime
                if product_data.get('expiration_date'):
                    product_data['expiration_date'] = datetime.fromisoformat(
                        product_data['expiration_date']
                    )
                product = Product(**product_data)
                self.products[product.id] = product

            self.transactions = data.get('transactions', [])
            print(f"📂 Inventario cargado desde {filename}")
            return True
        except FileNotFoundError:
            print(f"⚠️  Archivo {filename} no encontrado")
            return False
        except Exception as e:
            print(f"❌ Error al cargar inventario: {e}")
            return False


def example_usage():
    """Ejemplo de uso del sistema de inventario"""
    print("🏥 SISTEMA DE GESTIÓN DE INVENTARIO - FARMACIA NIETO\n")

    # Crear gestor de inventario
    inventory = InventoryManager()

    # Agregar productos de ejemplo
    products = [
        Product(
            id="PROD001",
            name="Vitamina C 1000mg",
            category=ProductCategory.ORTOMOLECULAR,
            description="Ácido ascórbico de alta pureza",
            stock_quantity=50,
            min_stock=10,
            unit_price=2500.00,
            expiration_date=datetime.now() + timedelta(days=180),
            batch_number="VC2024-001",
            supplier="Laboratorio XYZ",
            storage_location="Estante A-1"
        ),
        Product(
            id="PROD002",
            name="Crema Hidratante Personalizada",
            category=ProductCategory.DERMOCOSMETICA,
            description="Crema facial con ácido hialurónico",
            stock_quantity=5,
            min_stock=8,
            unit_price=3500.00,
            expiration_date=datetime.now() + timedelta(days=90),
            batch_number="CH2024-002",
            supplier="Materia Prima ABC",
            storage_location="Refrigerador B"
        ),
        Product(
            id="PROD003",
            name="Arnica Montana 30CH",
            category=ProductCategory.HOMEOPATIA,
            description="Glóbulos homeopáticos",
            stock_quantity=25,
            min_stock=5,
            unit_price=1800.00,
            expiration_date=datetime.now() + timedelta(days=365),
            batch_number="AM2024-003"
        )
    ]

    for product in products:
        inventory.add_product(product)

    print("\n" + "─" * 64 + "\n")

    # Realizar algunas operaciones
    print("📦 Actualizando stock...")
    inventory.update_stock("PROD001", -10, "Venta")
    inventory.update_stock("PROD002", 3, "Nueva elaboración")

    print("\n" + "─" * 64 + "\n")

    # Buscar productos
    print("🔍 Buscando productos con 'Vitamina'...")
    results = inventory.search_products("Vitamina")
    for product in results:
        print(f"   Encontrado: {product.name} - Stock: {product.stock_quantity}")

    print("\n" + "─" * 64 + "\n")

    # Generar reporte
    print(inventory.generate_stock_report())

    # Guardar inventario
    inventory.save_to_file("farmacia_nieto_inventory.json")


if __name__ == "__main__":
    example_usage()

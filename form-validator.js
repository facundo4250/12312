/**
 * Validador de Formularios - Farmacia Nieto
 * Sistema de validación y gestión de formularios de contacto
 * @author Código de Ejemplo
 * @version 1.0.0
 */

class FormValidator {
    constructor(formId) {
        this.form = document.getElementById(formId);
        this.errors = {};
        this.init();
    }

    /**
     * Inicializa el validador de formularios
     */
    init() {
        if (!this.form) {
            console.error(`Formulario con ID "${formId}" no encontrado`);
            return;
        }

        this.form.addEventListener('submit', (e) => this.handleSubmit(e));
        this.addRealTimeValidation();
    }

    /**
     * Valida el correo electrónico
     * @param {string} email - Email a validar
     * @returns {boolean}
     */
    validateEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    /**
     * Valida el teléfono argentino
     * @param {string} phone - Teléfono a validar
     * @returns {boolean}
     */
    validatePhone(phone) {
        // Acepta formatos: +54 291 432-7031, 291-432-7031, 2914327031
        const phoneRegex = /^(\+54\s?)?[\d\s\-]{8,15}$/;
        return phoneRegex.test(phone);
    }

    /**
     * Valida que un campo no esté vacío
     * @param {string} value - Valor a validar
     * @returns {boolean}
     */
    validateRequired(value) {
        return value.trim().length > 0;
    }

    /**
     * Valida la longitud mínima
     * @param {string} value - Valor a validar
     * @param {number} minLength - Longitud mínima
     * @returns {boolean}
     */
    validateMinLength(value, minLength) {
        return value.trim().length >= minLength;
    }

    /**
     * Muestra un error en el campo
     * @param {HTMLElement} field - Campo del formulario
     * @param {string} message - Mensaje de error
     */
    showError(field, message) {
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message';
        errorDiv.style.color = '#e74c3c';
        errorDiv.style.fontSize = '0.9rem';
        errorDiv.style.marginTop = '0.5rem';
        errorDiv.textContent = message;

        // Remover error previo si existe
        this.clearError(field);

        // Agregar borde rojo al campo
        field.style.borderColor = '#e74c3c';

        // Insertar mensaje de error
        field.parentElement.appendChild(errorDiv);

        this.errors[field.id] = message;
    }

    /**
     * Limpia los errores de un campo
     * @param {HTMLElement} field - Campo del formulario
     */
    clearError(field) {
        const existingError = field.parentElement.querySelector('.error-message');
        if (existingError) {
            existingError.remove();
        }
        field.style.borderColor = 'rgba(255,255,255,0.3)';
        delete this.errors[field.id];
    }

    /**
     * Valida todos los campos del formulario
     * @returns {boolean}
     */
    validateForm() {
        this.errors = {};
        let isValid = true;

        const nameField = this.form.querySelector('#name');
        const emailField = this.form.querySelector('#email');
        const phoneField = this.form.querySelector('#phone');
        const messageField = this.form.querySelector('#message');

        // Validar nombre
        if (nameField && !this.validateRequired(nameField.value)) {
            this.showError(nameField, 'El nombre es requerido');
            isValid = false;
        } else if (nameField && !this.validateMinLength(nameField.value, 3)) {
            this.showError(nameField, 'El nombre debe tener al menos 3 caracteres');
            isValid = false;
        } else if (nameField) {
            this.clearError(nameField);
        }

        // Validar email (opcional pero si se provee debe ser válido)
        if (emailField && emailField.value.trim() !== '' && !this.validateEmail(emailField.value)) {
            this.showError(emailField, 'Email inválido');
            isValid = false;
        } else if (emailField) {
            this.clearError(emailField);
        }

        // Validar teléfono
        if (phoneField && !this.validateRequired(phoneField.value)) {
            this.showError(phoneField, 'El teléfono es requerido');
            isValid = false;
        } else if (phoneField && !this.validatePhone(phoneField.value)) {
            this.showError(phoneField, 'Teléfono inválido. Formato: +54 291 432-7031');
            isValid = false;
        } else if (phoneField) {
            this.clearError(phoneField);
        }

        // Validar mensaje
        if (messageField && !this.validateRequired(messageField.value)) {
            this.showError(messageField, 'El mensaje es requerido');
            isValid = false;
        } else if (messageField && !this.validateMinLength(messageField.value, 10)) {
            this.showError(messageField, 'El mensaje debe tener al menos 10 caracteres');
            isValid = false;
        } else if (messageField) {
            this.clearError(messageField);
        }

        return isValid;
    }

    /**
     * Agrega validación en tiempo real
     */
    addRealTimeValidation() {
        const fields = this.form.querySelectorAll('input, textarea');
        fields.forEach(field => {
            field.addEventListener('blur', () => {
                this.validateForm();
            });

            field.addEventListener('input', () => {
                if (this.errors[field.id]) {
                    this.validateForm();
                }
            });
        });
    }

    /**
     * Maneja el envío del formulario
     * @param {Event} e - Evento de envío
     */
    handleSubmit(e) {
        e.preventDefault();

        if (!this.validateForm()) {
            console.log('Formulario inválido', this.errors);
            this.showNotification('Por favor corrige los errores en el formulario', 'error');
            return;
        }

        const formData = new FormData(this.form);
        this.sendToWhatsApp(formData);
    }

    /**
     * Envía los datos a WhatsApp
     * @param {FormData} formData - Datos del formulario
     */
    sendToWhatsApp(formData) {
        const name = formData.get('name');
        const email = formData.get('email');
        const phone = formData.get('phone');
        const service = formData.get('service');
        const message = formData.get('message');

        let whatsappMessage = `Hola, soy ${name}.%0A%0A`;
        whatsappMessage += `📧 Email: ${email || 'No proporcionado'}%0A`;
        whatsappMessage += `📞 Teléfono: ${phone}%0A`;

        if (service) {
            const serviceName = this.getServiceName(service);
            whatsappMessage += `🔬 Servicio de interés: ${serviceName}%0A`;
        }

        whatsappMessage += `%0A💬 Consulta:%0A${encodeURIComponent(message)}%0A%0A`;
        whatsappMessage += `Enviado desde el formulario web de Farmacia Nieto.`;

        const whatsappURL = `https://wa.me/5492914327031?text=${whatsappMessage}`;

        // Abrir WhatsApp
        window.open(whatsappURL, '_blank');

        // Mostrar notificación de éxito
        this.showNotification('¡Gracias por tu consulta! Te redirigiremos a WhatsApp.', 'success');

        // Limpiar formulario
        setTimeout(() => {
            this.form.reset();
        }, 1000);
    }

    /**
     * Obtiene el nombre del servicio
     * @param {string} serviceCode - Código del servicio
     * @returns {string}
     */
    getServiceName(serviceCode) {
        const services = {
            'ortomolecular': 'Medicina Ortomolecular',
            'dermocosmetica': 'Dermocosmética Especializada',
            'homeopatia': 'Homeopatía Clásica',
            'alopatica': 'Medicina Alopática Magistral',
            'fitoterapia': 'Fitoterapia Avanzada',
            'florales': 'Florales de Bach',
            'probioticos': 'Probióticos Especializados',
            'hormonas': 'Hormonas Bioidénticas',
            'asesoria': 'Análisis y Asesoramiento',
            'otro': 'Otro servicio'
        };
        return services[serviceCode] || serviceCode;
    }

    /**
     * Muestra una notificación
     * @param {string} message - Mensaje a mostrar
     * @param {string} type - Tipo de notificación (success, error, info)
     */
    showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `notification notification-${type}`;
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 1rem 2rem;
            background: ${type === 'success' ? '#27ae60' : type === 'error' ? '#e74c3c' : '#3498db'};
            color: white;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.2);
            z-index: 10000;
            animation: slideInRight 0.3s ease;
        `;
        notification.textContent = message;

        document.body.appendChild(notification);

        setTimeout(() => {
            notification.style.animation = 'slideOutRight 0.3s ease';
            setTimeout(() => {
                notification.remove();
            }, 300);
        }, 3000);
    }
}

// Inicializar el validador cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
    const validator = new FormValidator('contactForm');
});

// Exportar para uso en módulos
if (typeof module !== 'undefined' && module.exports) {
    module.exports = FormValidator;
}


<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Farmacia Nieto - Elaboración Magistral Personalizada | Bahía Blanca</title>
    <meta name="description" content="Farmacia especializada en elaboración magistral personalizada. 28+ años de experiencia. Patricia Victoria Nieto - Universidad de San Luis.">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:wght@400;500;600;700&display=swap');
        
        :root {
            --primary-green: #2c5530;
            --secondary-green: #4a8b3a;
            --accent-green: #6ba54a;
            --light-green: #e8f5e8;
            --dark-green: #1a3d1f;
            --gold: #d4af37;
            --light-gold: #f4e6a1;
            --white: #ffffff;
            --light-gray: #f8f9fa;
            --medium-gray: #6c757d;
            --dark-gray: #343a40;
            --whatsapp: #25D366;
            --shadow-light: 0 2px 15px rgba(0,0,0,0.08);
            --shadow-medium: 0 8px 30px rgba(0,0,0,0.12);
            --shadow-strong: 0 15px 40px rgba(0,0,0,0.15);
            --gradient-primary: linear-gradient(135deg, var(--primary-green), var(--secondary-green));
            --gradient-gold: linear-gradient(135deg, var(--gold), var(--light-gold));
            --transition-fast: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            --transition-smooth: all 0.5s cubic-bezier(0.4, 0, 0.2, 1);
        }

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        html {
            scroll-behavior: smooth;
        }

        body {
            font-family: 'Inter', sans-serif;
            line-height: 1.6;
            color: var(--dark-gray);
            background-color: var(--white);
            overflow-x: hidden;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
            padding: 0 2rem;
        }

        /* Navigation */
        .navbar {
            position: fixed;
            top: 0;
            width: 100%;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(20px);
            border-bottom: 1px solid rgba(255, 255, 255, 0.2);
            z-index: 1000;
            transition: var(--transition-fast);
            padding: 1rem 0;
        }

        .navbar.scrolled {
            background: rgba(255, 255, 255, 0.98);
            box-shadow: var(--shadow-light);
            padding: 0.5rem 0;
        }

        .nav-content {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .nav-logo {
            font-family: 'Playfair Display', serif;
            font-size: 1.8rem;
            font-weight: 700;
            color: var(--primary-green);
            text-decoration: none;
        }

        .nav-links {
            display: flex;
            list-style: none;
            gap: 2rem;
        }

        .nav-links a {
            text-decoration: none;
            color: var(--dark-gray);
            font-weight: 500;
            transition: var(--transition-fast);
            position: relative;
        }

        .nav-links a:hover {
            color: var(--secondary-green);
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: -5px;
            left: 0;
            width: 0;
            height: 2px;
            background: var(--gradient-primary);
            transition: var(--transition-fast);
        }

        .nav-links a:hover::after {
            width: 100%;
        }

        .mobile-menu-btn {
            display: none;
            background: none;
            border: none;
            font-size: 1.5rem;
            cursor: pointer;
            color: var(--primary-green);
        }

        /* Hero Section */
        .hero {
            height: 100vh;
            background: var(--gradient-primary);
            position: relative;
            display: flex;
            align-items: center;
            overflow: hidden;
        }

        .hero::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1000"><defs><pattern id="grain" width="100" height="100" patternUnits="userSpaceOnUse"><circle cx="20" cy="20" r="1" fill="white" opacity="0.1"/><circle cx="80" cy="80" r="1" fill="white" opacity="0.1"/><circle cx="40" cy="60" r="1" fill="white" opacity="0.1"/></pattern></defs><rect width="1000" height="1000" fill="url(%23grain)"/></svg>');
            opacity: 0.3;
        }

        .hero-particles {
            position: absolute;
            width: 100%;
            height: 100%;
            overflow: hidden;
        }

        .particle {
            position: absolute;
            background: rgba(255, 255, 255, 0.1);
            border-radius: 50%;
            animation: float 6s ease-in-out infinite;
        }

        .particle:nth-child(1) {
            width: 80px;
            height: 80px;
            left: 10%;
            animation-delay: 0s;
        }

        .particle:nth-child(2) {
            width: 120px;
            height: 120px;
            left: 20%;
            animation-delay: 2s;
        }

        .particle:nth-child(3) {
            width: 60px;
            height: 60px;
            left: 80%;
            animation-delay: 4s;
        }

        @keyframes float {
            0%, 100% { transform: translateY(0) rotate(0deg); }
            50% { transform: translateY(-20px) rotate(180deg); }
        }

        .hero-content {
            position: relative;
            z-index: 2;
            color: white;
            max-width: 800px;
        }

        .hero-title {
            font-family: 'Playfair Display', serif;
            font-size: clamp(3rem, 6vw, 5rem);
            font-weight: 700;
            margin-bottom: 1.5rem;
            line-height: 1.2;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            opacity: 0;
            animation: slideInUp 1s ease 0.5s forwards;
        }

        .hero-subtitle {
            font-size: clamp(1.2rem, 2.5vw, 1.5rem);
            margin-bottom: 2rem;
            opacity: 0.95;
            font-weight: 300;
            opacity: 0;
            animation: slideInUp 1s ease 0.7s forwards;
        }

        .hero-description {
            font-size: 1.1rem;
            margin-bottom: 3rem;
            opacity: 0.9;
            line-height: 1.7;
            opacity: 0;
            animation: slideInUp 1s ease 0.9s forwards;
        }

        .hero-cta {
            display: flex;
            gap: 1.5rem;
            flex-wrap: wrap;
            opacity: 0;
            animation: slideInUp 1s ease 1.1s forwards;
        }

        @keyframes slideInUp {
            from {
                opacity: 0;
                transform: translateY(30px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Buttons */
        .btn {
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            padding: 1rem 2rem;
            border: none;
            border-radius: 50px;
            font-weight: 600;
            text-decoration: none;
            transition: var(--transition-fast);
            cursor: pointer;
            font-size: 1rem;
            position: relative;
            overflow: hidden;
        }

        .btn::before {
            content: '';
            position: absolute;
            top: 0;
            left: -100%;
            width: 100%;
            height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
            transition: var(--transition-fast);
        }

        .btn:hover::before {
            left: 100%;
        }

        .btn-primary {
            background: var(--gradient-gold);
            color: var(--primary-green);
            box-shadow: var(--shadow-medium);
        }

        .btn-primary:hover {
            transform: translateY(-3px);
            box-shadow: var(--shadow-strong);
        }

        .btn-outline {
            background: transparent;
            color: white;
            border: 2px solid rgba(255,255,255,0.3);
            backdrop-filter: blur(10px);
        }

        .btn-outline:hover {
            background: rgba(255,255,255,0.1);
            border-color: rgba(255,255,255,0.6);
            transform: translateY(-3px);
        }

        .btn-whatsapp {
            background: var(--whatsapp);
            color: white;
            box-shadow: 0 4px 20px rgba(37, 211, 102, 0.3);
        }

        .btn-whatsapp:hover {
            background: #128C7E;
            transform: translateY(-3px);
            box-shadow: 0 8px 30px rgba(37, 211, 102, 0.4);
        }

        /* Professional Badge */
        .professional-badge {
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255,255,255,0.2);
            border-radius: 20px;
            padding: 2rem;
            margin-top: 3rem;
            text-align: center;
            opacity: 0;
            animation: slideInUp 1s ease 1.3s forwards;
        }

        .professional-badge h3 {
            font-family: 'Playfair Display', serif;
            font-size: 1.5rem;
            margin-bottom: 1rem;
            color: var(--gold);
        }

        /* Statistics Section */
        .stats {
            background: var(--light-gray);
            padding: 5rem 0;
            position: relative;
        }

        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 3rem;
        }

        .stat-card {
            text-align: center;
            padding: 2rem;
            background: white;
            border-radius: 20px;
            box-shadow: var(--shadow-light);
            transition: var(--transition-smooth);
            border-top: 4px solid var(--secondary-green);
        }

        .stat-card:hover {
            transform: translateY(-10px);
            box-shadow: var(--shadow-strong);
        }

        .stat-number {
            font-family: 'Playfair Display', serif;
            font-size: 3rem;
            font-weight: 700;
            color: var(--secondary-green);
            margin-bottom: 0.5rem;
            counter-reset: number;
        }

        .stat-label {
            font-weight: 600;
            color: var(--medium-gray);
            text-transform: uppercase;
            letter-spacing: 1px;
            font-size: 0.9rem;
        }

        /* Services Section */
        .services {
            padding: 6rem 0;
            background: white;
            position: relative;
        }

        .section-header {
            text-align: center;
            margin-bottom: 4rem;
        }

        .section-title {
            font-family: 'Playfair Display', serif;
            font-size: clamp(2.5rem, 5vw, 3.5rem);
            color: var(--primary-green);
            margin-bottom: 1rem;
        }

        .section-subtitle {
            font-size: 1.2rem;
            color: var(--medium-gray);
            max-width: 600px;
            margin: 0 auto;
        }

        .services-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
            gap: 2.5rem;
            margin-top: 4rem;
        }

        .service-card {
            background: white;
            border-radius: 25px;
            padding: 3rem;
            box-shadow: var(--shadow-light);
            transition: var(--transition-smooth);
            position: relative;
            overflow: hidden;
            border: 1px solid rgba(76, 139, 58, 0.1);
        }

        .service-card::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: var(--gradient-primary);
            transform: scaleX(0);
            transition: var(--transition-smooth);
        }

        .service-card:hover::before {
            transform: scaleX(1);
        }

        .service-card:hover {
            transform: translateY(-15px);
            box-shadow: var(--shadow-strong);
        }

        .service-icon {
            font-size: 3rem;
            margin-bottom: 1.5rem;
            display: block;
        }

        .service-title {
            font-family: 'Playfair Display', serif;
            font-size: 1.5rem;
            color: var(--primary-green);
            margin-bottom: 1rem;
            font-weight: 600;
        }

        .service-description {
            color: var(--medium-gray);
            line-height: 1.7;
            font-size: 1rem;
        }

        /* About Section */
        .about {
            background: var(--light-green);
            padding: 6rem 0;
            position: relative;
        }

        .about-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4rem;
            align-items: center;
        }

        .about-text h2 {
            font-family: 'Playfair Display', serif;
            font-size: 2.5rem;
            color: var(--primary-green);
            margin-bottom: 2rem;
        }

        .about-text p {
            font-size: 1.1rem;
            color: var(--medium-gray);
            margin-bottom: 1.5rem;
            line-height: 1.7;
        }

        .about-features {
            list-style: none;
        }

        .about-features li {
            display: flex;
            align-items: center;
            gap: 1rem;
            margin-bottom: 1rem;
            font-weight: 500;
        }

        .about-features li::before {
            content: '✓';
            background: var(--secondary-green);
            color: white;
            width: 24px;
            height: 24px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 0.8rem;
            font-weight: bold;
        }

        .about-image {
            background: var(--gradient-primary);
            border-radius: 25px;
            height: 400px;
            position: relative;
            overflow: hidden;
        }

        .about-image::before {
            content: '🧬';
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 8rem;
            opacity: 0.3;
        }

        /* Testimonials */
        .testimonials {
            padding: 6rem 0;
            background: white;
        }

        .testimonials-slider {
            max-width: 800px;
            margin: 0 auto;
            text-align: center;
        }

        .testimonial {
            background: var(--light-gray);
            padding: 3rem;
            border-radius: 25px;
            margin: 2rem 0;
            position: relative;
        }

        .testimonial::before {
            content: '"';
            font-family: 'Playfair Display', serif;
            font-size: 4rem;
            color: var(--secondary-green);
            position: absolute;
            top: -10px;
            left: 30px;
        }

        .testimonial-text {
            font-size: 1.2rem;
            font-style: italic;
            color: var(--dark-gray);
            margin-bottom: 2rem;
            line-height: 1.6;
        }

        .testimonial-author {
            font-weight: 600;
            color: var(--primary-green);
        }

        /* Contact Section */
        .contact {
            background: var(--gradient-primary);
            color: white;
            padding: 6rem 0;
            position: relative;
        }

        .contact-content {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 4rem;
            align-items: start;
        }

        .contact-info h2 {
            font-family: 'Playfair Display', serif;
            font-size: 2.5rem;
            margin-bottom: 2rem;
        }

        .contact-details {
            display: grid;
            gap: 2rem;
            margin-top: 2rem;
        }

        .contact-item {
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255,255,255,0.2);
            border-radius: 20px;
            padding: 2rem;
            transition: var(--transition-fast);
        }

        .contact-item:hover {
            background: rgba(255,255,255,0.15);
            transform: translateY(-5px);
        }

        .contact-item h4 {
            font-size: 1.2rem;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        .contact-item p {
            opacity: 0.9;
            line-height: 1.6;
        }

        .contact-form {
            background: rgba(255,255,255,0.1);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255,255,255,0.2);
            border-radius: 25px;
            padding: 3rem;
        }

        .form-group {
            margin-bottom: 2rem;
        }

        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
        }

        .form-group input,
        .form-group textarea {
            width: 100%;
            padding: 1rem;
            border: 1px solid rgba(255,255,255,0.3);
            border-radius: 15px;
            background: rgba(255,255,255,0.1);
            color: white;
            font-size: 1rem;
            transition: var(--transition-fast);
        }

        .form-group input:focus,
        .form-group textarea:focus {
            outline: none;
            border-color: var(--gold);
            background: rgba(255,255,255,0.15);
        }

        .form-group input::placeholder,
        .form-group textarea::placeholder {
            color: rgba(255,255,255,0.7);
        }

        /* Footer */
        .footer {
            background: var(--dark-green);
            color: white;
            padding: 4rem 0 2rem;
        }

        .footer-content {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 3rem;
            margin-bottom: 3rem;
        }

        .footer-section h4 {
            font-family: 'Playfair Display', serif;
            font-size: 1.3rem;
            margin-bottom: 1.5rem;
            color: var(--gold);
        }

        .footer-section p {
            margin-bottom: 0.8rem;
            line-height: 1.6;
            opacity: 0.9;
        }

        .footer-bottom {
            text-align: center;
            padding-top: 2rem;
            border-top: 1px solid rgba(255,255,255,0.2);
            opacity: 0.8;
        }

        /* Scroll Animations */
        .fade-in {
            opacity: 0;
            transform: translateY(30px);
            transition: var(--transition-smooth);
        }

        .fade-in.visible {
            opacity: 1;
            transform: translateY(0);
        }

        /* Loading Animation */
        .loading-screen {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: var(--gradient-primary);
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 9999;
            transition: var(--transition-smooth);
        }

        .loading-screen.hidden {
            opacity: 0;
            visibility: hidden;
        }

        .loader {
            width: 60px;
            height: 60px;
            border: 3px solid rgba(255,255,255,0.3);
            border-top: 3px solid white;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }

        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .nav-links {
                display: none;
            }

            .mobile-menu-btn {
                display: block;
            }

            .hero-content {
                text-align: center;
                padding: 0 1rem;
            }

            .hero-cta {
                justify-content: center;
            }

            .services-grid {
                grid-template-columns: 1fr;
            }

            .service-card {
                padding: 2rem;
            }

            .about-content {
                grid-template-columns: 1fr;
                text-align: center;
            }

            .contact-content {
                grid-template-columns: 1fr;
            }

            .stats-grid {
                grid-template-columns: repeat(2, 1fr);
            }

            .container {
                padding: 0 1rem;
            }
        }

        @media (max-width: 480px) {
            .stats-grid {
                grid-template-columns: 1fr;
            }
            
            .services-grid {
                grid-template-columns: 1fr;
            }
            
            .service-card {
                min-width: unset;
            }
        }

        /* Accessibility */
        @media (prefers-reduced-motion: reduce) {
            * {
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
            }
        }

        /* Print Styles */
        @media print {
            .navbar, .loading-screen {
                display: none;
            }
            
            .hero {
                height: auto;
                padding: 2rem 0;
            }
        }
    </style>
</head>
<body>
    <!-- Loading Screen -->
    <div class="loading-screen" id="loadingScreen">
        <div class="loader"></div>
    </div>

    <!-- Navigation -->
    <nav class="navbar" id="navbar">
        <div class="container">
            <div class="nav-content">
                <a href="#home" class="nav-logo">Farmacia Nieto</a>
                <ul class="nav-links">
                    <li><a href="#home">Inicio</a></li>
                    <li><a href="#services">Servicios</a></li>
                    <li><a href="#about">Nosotros</a></li>
                    <li><a href="#contact">Contacto</a></li>
                </ul>
                <button class="mobile-menu-btn" id="mobileMenuBtn">☰</button>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero" id="home">
        <div class="hero-particles">
            <div class="particle"></div>
            <div class="particle"></div>
            <div class="particle"></div>
        </div>
        <div class="container">
            <div class="hero-content">
                <h1 class="hero-title">Elaboración Magistral Personalizada</h1>
                <p class="hero-subtitle">Tu camino hacia el bienestar desde 1996</p>
                <p class="hero-description">
                    Bajo la dirección técnica de Patricia Victoria Nieto, farmacéutica egresada de la Universidad de San Luis con más de 28 años de experiencia, te ofrecemos productos de la más alta calidad y una atención personalizada excepcional para cuidar tu salud de manera integral.
                </p>
                <div class="hero-cta">
                    <a href="https://wa.me/5492914327031?text=Hola,%20me%20interesa%20conocer%20más%20sobre%20sus%20servicios%20de%20elaboración%20magistral%20personalizada" target="_blank" class="btn btn-whatsapp">
                        💬 Consultar por WhatsApp
                    </a>
                    <a href="#services" class="btn btn-outline">
                        🔬 Ver Servicios
                    </a>
                </div>

                <div class="professional-badge">
                    <h3>🎓 Farmacéutica Profesional Certificada</h3>
                    <p>Formulaciones personalizadas según las necesidades específicas de cada paciente</p>
                </div>
            </div>
        </div>
    </section>

    <!-- Statistics Section -->
    <section class="stats fade-in">
        <div class="container">
            <div class="stats-grid">
                <div class="stat-card">
                    <div class="stat-number" data-target="28">0</div>
                    <div class="stat-label">Años de Experiencia</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" data-target="5000">0</div>
                    <div class="stat-label">Pacientes Atendidos</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" data-target="9">0</div>
                    <div class="stat-label">Especialidades Médicas</div>
                </div>
                <div class="stat-card">
                    <div class="stat-number" data-target="100">0</div>
                    <div class="stat-label">% Satisfacción</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Services Section -->
    <section class="services fade-in" id="services">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">Nuestros Servicios Especializados</h2>
                <p class="section-subtitle">
                    Ofrecemos una amplia gama de tratamientos personalizados con los más altos estándares de calidad farmacéutica
                </p>
            </div>
            
            <div class="services-grid">
                <div class="service-card">
                    <span class="service-icon">🧬</span>
                    <h3 class="service-title">Medicina Ortomolecular</h3>
                    <p class="service-description">
                        Tratamientos personalizados basados en el equilibrio molecular óptimo para restaurar la salud natural del organismo mediante nutrientes específicos y suplementación dirigida.
                    </p>
                </div>

                <div class="service-card">
                    <span class="service-icon">💆‍♀️</span>
                    <h3 class="service-title">Dermocosmética Especializada</h3>
                    <p class="service-description">
                        Productos especializados para el cuidado de la piel, formulados específicamente para cada tipo y necesidad. Tratamientos anti-edad, acné, rosácea y más.
                    </p>
                </div>

                <div class="service-card">
                    <span class="service-icon">🌿</span>
                    <h3 class="service-title">Homeopatía Clásica</h3>
                    <p class="service-description">
                        Preparaciones homeopáticas tradicionales elaboradas con los más altos estándares de calidad y pureza, siguiendo los principios de la medicina homeopática clásica.
                    </p>
                </div>

                <div class="service-card">
                    <span class="service-icon">💊</span>
                    <h3 class="service-title">Medicina Alopática Magistral</h3>
                    <p class="service-description">
                        Medicamentos alopáticos preparados magistralmente según prescripción médica con máxima precisión. Dosificaciones personalizadas y formas farmacéuticas adaptadas a cada paciente.
                    </p>
                </div>

                <div class="service-card">
                    <span class="service-icon">🌱</span>
                    <h3 class="service-title">Fitoterapia Avanzada</h3>
                    <p class="service-description">
                        Tratamientos naturales a base de plantas medicinales, respaldados por la tradición milenaria y la ciencia moderna. Extractos estandarizados y tinturas madre de alta calidad.
                    </p>
                </div>

                <div class="service-card">
                    <span class="service-icon">🌸</span>
                    <h3 class="service-title">Florales de Bach</h3>
                    <p class="service-description">
                        Esencias florales de Bach y otros sistemas florales para el equilibrio emocional y el bienestar integral. Fórmulas personalizadas según el estado emocional de cada persona.
                    </p>
                </div>

                <div class="service-card">
                    <span class="service-icon">🦠</span>
                    <h3 class="service-title">Probióticos Especializados</h3>
                    <p class="service-description">
                        Formulaciones probióticas específicas para restaurar y mantener el equilibrio de la flora intestinal. Cepas seleccionadas según necesidades digestivas individuales.
                    </p>
                </div>

                <div class="service-card">
                    <span class="service-icon">⚖️</span>
                    <h3 class="service-title">Hormonas Bioidénticas</h3>
                    <p class="service-description">
                        Terapias hormonales personalizadas con hormonas bioidénticas para el equilibrio hormonal natural. Tratamientos para menopausia, andropausia y desequilibrios hormonales.
                    </p>
                </div>

                <div class="service-card">
                    <span class="service-icon">🔬</span>
                    <h3 class="service-title">Análisis y Asesoramiento</h3>
                    <p class="service-description">
                        Consultoría farmacéutica especializada, análisis de medicamentos, interacciones farmacológicas y asesoramiento profesional personalizado para optimizar tratamientos.
                    </p>
                </div>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section class="about fade-in" id="about">
        <div class="container">
            <div class="about-content">
                <div class="about-text">
                    <h2>Excelencia en Farmacia Magistral</h2>
                    <p>
                        Con más de 28 años de dedicación y experiencia en el campo farmacéutico, la Dra. Patricia Victoria Nieto, egresada de la Universidad de San Luis, lidera nuestro equipo con un compromiso inquebrantable hacia la excelencia y la innovación en elaboración magistral.
                    </p>
                    <p>
                        Nuestro laboratorio farmacéutico cuenta con tecnología de vanguardia y cumple con las más estrictas normas de calidad farmacéutica, garantizando la máxima eficacia y seguridad en cada preparación.
                    </p>
                    
                    <ul class="about-features">
                        <li>Laboratorio certificado con tecnología de última generación</li>
                        <li>Personal farmacéutico altamente calificado y actualizado</li>
                        <li>Materia prima de origen farmacéutico certificado</li>
                        <li>Control de calidad riguroso en cada preparación</li>
                        <li>Asesoramiento profesional personalizado</li>
                        <li>Seguimiento post-tratamiento de pacientes</li>
                        <li>Formación continua en nuevas terapias</li>
                        <li>Colaboración con médicos especialistas</li>
                    </ul>

                    <div style="margin-top: 2rem;">
                        <a href="https://wa.me/5492914327031?text=Hola,%20me%20gustaría%20conocer%20más%20sobre%20la%20experiencia%20y%20certificaciones%20de%20la%20farmacia" target="_blank" class="btn btn-primary">
                            📋 Conocer Más Detalles
                        </a>
                    </div>
                </div>
                <div class="about-image">
                    <!-- Decorative background with molecular structure -->
                </div>
            </div>
        </div>
    </section>

    <!-- Testimonials Section -->
    <section class="testimonials fade-in">
        <div class="container">
            <div class="section-header">
                <h2 class="section-title">Lo Que Dicen Nuestros Pacientes</h2>
                <p class="section-subtitle">La confianza de nuestros pacientes es nuestro mayor logro</p>
            </div>
            
            <div class="testimonials-slider">
                <div class="testimonial">
                    <p class="testimonial-text">
                        "Después de años de problemas hormonales, encontré en la Farmacia Nieto la solución personalizada que necesitaba. La atención profesional y el seguimiento personalizado han sido excepcionales."
                    </p>
                    <div class="testimonial-author">- María Elena R., Bahía Blanca</div>
                </div>
                
                <div class="testimonial">
                    <p class="testimonial-text">
                        "Los productos dermatológicos preparados especialmente para mi tipo de piel han transformado completamente mi rutina de cuidado. La diferencia es notable y duradera."
                    </p>
                    <div class="testimonial-author">- Carlos M., Médico Dermatólogo</div>
                </div>
                
                <div class="testimonial">
                    <p class="testimonial-text">
                        "La medicina ortomolecular personalizada me ayudó a recuperar mi energía y vitalidad. El profesionalismo y conocimiento de Patricia es extraordinario."
                    </p>
                    <div class="testimonial-author">- Ana Patricia L., Paciente</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Contact Section -->
    <section class="contact fade-in" id="contact">
        <div class="container">
            <div class="contact-content">
                <div class="contact-info">
                    <h2>Contactanos para una Consulta Personalizada</h2>
                    <p>Estamos aquí para ayudarte a encontrar la solución farmacéutica perfecta para tus necesidades específicas. Nuestro equipo de profesionales está listo para brindarte la atención especializada que mereces.</p>
                    
                    <div class="contact-details">
                        <div class="contact-item">
                            <h4>💬 WhatsApp</h4>
                            <p>(+54) 291432-7031</p>
                            <a href="https://wa.me/5492914327031?text=Hola,%20me%20interesa%20conocer%20más%20sobre%20sus%20servicios%20de%20elaboración%20magistral%20personalizada" target="_blank" class="btn btn-whatsapp" style="margin-top: 1rem;">
                                Contactar por WhatsApp
                            </a>
                        </div>
                        
                        <div class="contact-item">
                            <h4>📧 Email Profesional</h4>
                            <p>farmacia.nieto@hotmail.com</p>
                            <p style="font-size: 0.9rem; opacity: 0.8;">Respuesta en menos de 24 horas</p>
                        </div>
                        
                        <div class="contact-item">
                            <h4>📍 Ubicación</h4>
                            <p>Bahía Blanca, Buenos Aires, Argentina</p>
                            <p style="font-size: 0.9rem; opacity: 0.8;">Consultas presenciales con cita previa</p>
                        </div>
                        
                        <div class="contact-item">
                            <h4>🕐 Horarios de Atención</h4>
                            <p><strong>Lunes a Viernes:</strong> 8:00 - 20:00 hs</p>
                            <p><strong>Sábados:</strong> 8:00 - 13:00 hs</p>
                            <p style="font-size: 0.9rem; opacity: 0.8;">Emergencias: Contactar por WhatsApp</p>
                        </div>
                    </div>
                </div>
                
                <div class="contact-form">
                    <h3 style="margin-bottom: 2rem; font-family: 'Playfair Display', serif;">Envíanos tu Consulta</h3>
                    <form id="contactForm">
                        <div class="form-group">
                            <label for="name">Nombre Completo *</label>
                            <input type="text" id="name" name="name" placeholder="Tu nombre completo" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="email">Email</label>
                            <input type="email" id="email" name="email" placeholder="tu@email.com">
                        </div>
                        
                        <div class="form-group">
                            <label for="phone">Teléfono *</label>
                            <input type="tel" id="phone" name="phone" placeholder="+54 291 xxx-xxxx" required>
                        </div>
                        
                        <div class="form-group">
                            <label for="service">Servicio de Interés</label>
                            <select id="service" name="service" style="width: 100%; padding: 1rem; border: 1px solid rgba(255,255,255,0.3); border-radius: 15px; background: rgba(255,255,255,0.1); color: white; font-size: 1rem;">
                                <option value="">Seleccionar servicio...</option>
                                <option value="ortomolecular">Medicina Ortomolecular</option>
                                <option value="dermocosmetica">Dermocosmética Especializada</option>
                                <option value="homeopatia">Homeopatía Clásica</option>
                                <option value="alopatica">Medicina Alopática Magistral</option>
                                <option value="fitoterapia">Fitoterapia Avanzada</option>
                                <option value="florales">Florales de Bach</option>
                                <option value="probioticos">Probióticos Especializados</option>
                                <option value="hormonas">Hormonas Bioidénticas</option>
                                <option value="asesoria">Análisis y Asesoramiento</option>
                                <option value="otro">Otro servicio</option>
                            </select>
                        </div>
                        
                        <div class="form-group">
                            <label for="message">Mensaje *</label>
                            <textarea id="message" name="message" rows="4" placeholder="Describe tu consulta o necesidad específica..." required></textarea>
                        </div>
                        
                        <button type="submit" class="btn btn-primary" style="width: 100%;">
                            📨 Enviar Consulta
                        </button>
                    </form>
                </div>
            </div>
        </div>
    </section>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h4>Farmacia Nieto</h4>
                    <p>Tu camino hacia el bienestar desde 1996.</p>
                    <p>Elaboración magistral personalizada con la más alta calidad farmacéutica y atención profesional excepcional.</p>
                    <p>Comprometidos con tu salud y bienestar integral a través de tratamientos personalizados y seguimiento profesional.</p>
                </div>

                <div class="footer-section">
                    <h4>Servicios Especializados</h4>
                    <p>• Medicina Ortomolecular Personalizada</p>
                    <p>• Dermocosmética Especializada</p>
                    <p>• Homeopatía y Alopatía Magistral</p>
                    <p>• Fitoterapia Natural Avanzada</p>
                    <p>• Florales de Bach y Terapias Florales</p>
                    <p>• Probióticos y Hormonas Bioidénticas</p>
                    <p>• Análisis y Asesoramiento Farmacéutico</p>
                </div>

                <div class="footer-section">
                    <h4>Información de Contacto</h4>
                    <p>📱 <strong>WhatsApp:</strong> (+54) 291432-7031</p>
                    <p>✉️ <strong>Email:</strong> farmacia.nieto@hotmail.com</p>
                    <p>📍 <strong>Ubicación:</strong> Bahía Blanca, Buenos Aires, Argentina</p>
                    <p>⏰ <strong>Horarios:</strong></p>
                    <p>&nbsp;&nbsp;&nbsp;Lun-Vie: 8:00-20:00 hs</p>
                    <p>&nbsp;&nbsp;&nbsp;Sáb: 8:00-13:00 hs</p>
                </div>

                <div class="footer-section">
                    <h4>Dirección Profesional</h4>
                    <p><strong>Directora Técnica:</strong> Patricia Victoria Nieto</p>
                    <p><strong>Formación:</strong> Universidad de San Luis</p>
                    <p><strong>Matrícula:</strong> Profesional Habilitada</p>
                    <p><strong>Experiencia:</strong> 28+ años en Farmacia</p>
                    <p><strong>Especialización:</strong> Elaboración Magistral Personalizada</p>
                    <p><strong>Certificaciones:</strong> Homeopatía, Fitoterapia, Medicina Ortomolecular</p>
                </div>
            </div>

            <div class="footer-bottom">
                <p>&copy; 2025 Farmacia Nieto - Patricia Victoria Nieto. Todos los derechos reservados.</p>
                <p>Elaboración Magistral Personalizada | Bahía Blanca, Buenos Aires, Argentina</p>
                <p>Matrícula Profesional Habilitada | Universidad de San Luis</p>
            </div>
        </div>
    </footer>

    <script>
        // Loading Screen
        window.addEventListener('load', function() {
            const loadingScreen = document.getElementById('loadingScreen');
            setTimeout(() => {
                loadingScreen.classList.add('hidden');
            }, 1500);
        });

        // Navbar Scroll Effect
        window.addEventListener('scroll', function() {
            const navbar = document.getElementById('navbar');
            if (window.scrollY > 100) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
        });

        // Smooth Scrolling for Navigation Links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });

        // Intersection Observer for Fade-in Animation
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, observerOptions);

        document.querySelectorAll('.fade-in').forEach(el => {
            observer.observe(el);
        });

        // Counter Animation for Statistics
        function animateCounter(element, target) {
            let current = 0;
            const increment = target / 100;
            const timer = setInterval(() => {
                current += increment;
                if (current >= target) {
                    current = target;
                    clearInterval(timer);
                }
                element.textContent = Math.floor(current);
            }, 20);
        }

        // Animate counters when stats section becomes visible
        const statsObserver = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const counters = entry.target.querySelectorAll('.stat-number');
                    counters.forEach(counter => {
                        const target = parseInt(counter.getAttribute('data-target'));
                        animateCounter(counter, target);
                    });
                    statsObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.5 });

        const statsSection = document.querySelector('.stats');
        if (statsSection) {
            statsObserver.observe(statsSection);
        }

        // Contact Form Handling
        document.getElementById('contactForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            const formData = new FormData(this);
            const name = formData.get('name');
            const email = formData.get('email');
            const phone = formData.get('phone');
            const service = formData.get('service');
            const message = formData.get('message');
            
            // Construct WhatsApp message
            let whatsappMessage = `Hola, soy ${name}.%0A%0A`;
            whatsappMessage += `📧 Email: ${email}%0A`;
            whatsappMessage += `📞 Teléfono: ${phone}%0A`;
            
            if (service) {
                whatsappMessage += `🔬 Servicio de interés: ${service}%0A`;
            }
            
            whatsappMessage += `%0A💬 Consulta:%0A${message}%0A%0A`;
            whatsappMessage += `Enviado desde el formulario web de Farmacia Nieto.`;
            
            // Open WhatsApp with pre-filled message
            const whatsappURL = `https://wa.me/5492914327031?text=${whatsappMessage}`;
            window.open(whatsappURL, '_blank');
            
            // Show success message
            alert('¡Gracias por tu consulta! Te redirigiremos a WhatsApp para completar el contacto.');
            
            // Reset form
            this.reset();
        });

        // Mobile Menu Toggle (Basic implementation)
        document.getElementById('mobileMenuBtn').addEventListener('click', function() {
            const navLinks = document.querySelector('.nav-links');
            navLinks.style.display = navLinks.style.display === 'flex' ? 'none' : 'flex';
        });

        // Parallax Effect for Hero Section
        window.addEventListener('scroll', function() {
            const scrolled = window.pageYOffset;
            const parallax = document.querySelector('.hero');
            const speed = 0.5;
            
            if (parallax) {
                parallax.style.transform = `translateY(${scrolled * speed}px)`;
            }
        });

        // Service Cards Hover Effect Enhancement
        document.querySelectorAll('.service-card').forEach(card => {
            card.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-15px) scale(1.02)';
            });
            
            card.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0) scale(1)';
            });
        });

        // Add dynamic year to footer
        document.addEventListener('DOMContentLoaded', function() {
            const currentYear = new Date().getFullYear();
            document.querySelector('.footer-bottom p').innerHTML = 
                document.querySelector('.footer-bottom p').innerHTML.replace('2025', currentYear);
        });

        // Testimonials Auto-rotation (Basic implementation)
        let currentTestimonial = 0;
        const testimonials = document.querySelectorAll('.testimonial');
        
        function rotateTestimonials() {
            testimonials.forEach((testimonial, index) => {
                testimonial.style.display = index === currentTestimonial ? 'block' : 'none';
            });
            currentTestimonial = (currentTestimonial + 1) % testimonials.length;
        }

        // Initialize testimonials rotation
        if (testimonials.length > 0) {
            rotateTestimonials();
            setInterval(rotateTestimonials, 5000); // Rotate every 5 seconds
        }

        // Enhanced scroll animations for service cards
        const serviceCards = document.querySelectorAll('.service-card');
        serviceCards.forEach((card, index) => {
            card.style.animationDelay = `${index * 0.1}s`;
        });

        // Add performance optimizations
        let ticking = false;
        
        function updateOnScroll() {
            // Navbar scroll effect
            const navbar = document.getElementById('navbar');
            if (window.scrollY > 100) {
                navbar.classList.add('scrolled');
            } else {
                navbar.classList.remove('scrolled');
            }
            
            ticking = false;
        }
        
        window.addEventListener('scroll', function() {
            if (!ticking) {
                requestAnimationFrame(updateOnScroll);
                ticking = true;
            }
        });
    </script>
</body>
</html>

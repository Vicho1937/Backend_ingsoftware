import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import api from '../services/api'
import RouteCard from '../components/RouteCard'
import '../styles/Home.css'

function Home() {
  const { user } = useAuth()
  const [featuredRoutes, setFeaturedRoutes] = useState([])
  const [categories, setCategories] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    loadData()
  }, [])

  const loadData = async () => {
    try {
      const [routesRes, categoriesRes] = await Promise.all([
        api.get('/routes/?page_size=6'),
        api.get('/categories/')
      ])
      
      setFeaturedRoutes(routesRes.data.results || routesRes.data)
      setCategories(categoriesRes.data.results || categoriesRes.data)
    } catch (error) {
      console.error('Error loading data:', error)
    } finally {
      setLoading(false)
    }
  }

  if (loading) {
    return <div className="loading">Cargando...</div>
  }

  return (
    <div className="home">
      <section className="hero">
        <div className="hero-overlay"></div>
        <div className="hero-content">
          <span className="hero-badge">✨ Descubre Santiago</span>
          <h1>Explora los Mejores Lugares de tu Ciudad</h1>
          <p>Más de {featuredRoutes.length}+ lugares verificados, reseñas reales y recomendaciones personalizadas</p>
          {!user && (
            <div className="hero-login-hint">
              <p>🔓 <Link to="/login" style={{color: 'var(--primary-color)', textDecoration: 'underline'}}>Inicia sesión</Link> para guardar favoritos, dejar reseñas y obtener recomendaciones personalizadas</p>
            </div>
          )}
          <div className="hero-buttons">
            <Link to="/routes" className="btn-primary">
              🗺️ Explorar Lugares
            </Link>
            <Link to="/chat" className="btn-secondary-outline">
              💬 Preguntar al Asistente
            </Link>
          </div>
          <div className="hero-stats">
            <div className="stat-item">
              <span className="stat-number">{categories.length}+</span>
              <span className="stat-label">Categorías</span>
            </div>
            <div className="stat-item">
              <span className="stat-number">{featuredRoutes.length * 5}+</span>
              <span className="stat-label">Lugares</span>
            </div>
            <div className="stat-item">
              <span className="stat-number">1000+</span>
              <span className="stat-label">Reseñas</span>
            </div>
          </div>
        </div>
      </section>

      <section className="categories-section">
        <div className="section-header">
          <h2>🎯 Explora por Categoría</h2>
          <p>Encuentra exactamente lo que buscas</p>
        </div>
        <div className="categories-grid">
          {categories.slice(0, 8).map((category) => (
            <Link 
              key={category.id} 
              to={`/routes?category=${category.id}`}
              className="category-card"
            >
              <div className="category-icon-wrapper">
                <span className="category-icon">{category.icon || '📍'}</span>
              </div>
              <div className="category-info">
                <h3>{category.name}</h3>
                <p>{category.routes_count || 0} lugares</p>
              </div>
              <span className="category-arrow">→</span>
            </Link>
          ))}
        </div>
      </section>

      <section className="featured-section">
        <div className="section-header">
          <h2>⭐ Lugares Destacados</h2>
          <p>Los favoritos de nuestra comunidad</p>
        </div>
        <div className="routes-grid">
          {featuredRoutes.map((route) => (
            <RouteCard key={route.id} route={route} />
          ))}
        </div>
        <div className="text-center">
          <Link to="/routes" className="btn-view-all">
            Ver Todos los Lugares
            <span className="arrow-icon">→</span>
          </Link>
        </div>
      </section>

      <section className="features-section">
        <div className="section-header">
          <h2>💎 ¿Por qué usar Ruta Local?</h2>
          <p>La mejor forma de descubrir tu ciudad</p>
        </div>
        <div className="features-grid">
          <div className="feature-card">
            <div className="feature-icon-bg">
              <span className="feature-icon">🗺️</span>
            </div>
            <h3>Explora</h3>
            <p>Descubre lugares únicos y auténticos cerca de ti con información verificada</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon-bg">
              <span className="feature-icon">⭐</span>
            </div>
            <h3>Califica y Opina</h3>
            <p>Comparte tu experiencia y ayuda a otros viajeros a tomar mejores decisiones</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon-bg">
              <span className="feature-icon">❤️</span>
            </div>
            <h3>Guarda Favoritos</h3>
            <p>Crea tu lista personalizada de lugares para visitar y nunca pierdas una recomendación</p>
          </div>
          <div className="feature-card">
            <div className="feature-icon-bg">
              <span className="feature-icon">🤖</span>
            </div>
            <h3>Asistente IA</h3>
            <p>Pregunta lo que quieras a nuestro chatbot inteligente sobre cualquier lugar</p>
          </div>
        </div>
      </section>

      {!user && (
        <section className="cta-section">
          <div className="cta-content">
            <h2>🚀 Comienza a Explorar Ahora</h2>
            <p>Únete a miles de usuarios que ya descubrieron nuevos lugares increíbles</p>
            <Link to="/register" className="btn-cta">
              Crear Cuenta Gratis
            </Link>
          </div>
        </section>
      )}
    </div>
  )
}

export default Home

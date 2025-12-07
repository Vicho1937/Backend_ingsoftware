import { useEffect, useState } from 'react'
import { useSearchParams } from 'react-router-dom'
import { Search, MapPin, Filter, Map, List, X } from 'lucide-react'
import api from '../services/api'
import RouteCard from '../components/RouteCard'
import MapView from '../components/MapView'
import NearbyPlaces from '../components/NearbyPlaces'
import '../styles/Routes.css'

function Routes() {
  const [routes, setRoutes] = useState([])
  const [categories, setCategories] = useState([])
  const [loading, setLoading] = useState(true)
  const [searchParams, setSearchParams] = useSearchParams()
  const [filters, setFilters] = useState({
    search: searchParams.get('search') || '',
    category: searchParams.get('category') || '',
    ordering: '-created_at'
  })
  const [showMap, setShowMap] = useState(false)
  const [suggestions, setSuggestions] = useState([])
  const [showSuggestions, setShowSuggestions] = useState(false)
  const [userLocation, setUserLocation] = useState(null)

  useEffect(() => {
    loadCategories()
    getUserLocation()
  }, [])

  useEffect(() => {
    loadRoutes()
  }, [filters])

  const getUserLocation = () => {
    if (navigator.geolocation) {
      navigator.geolocation.getCurrentPosition(
        (position) => {
          setUserLocation([position.coords.latitude, position.coords.longitude])
        },
        (error) => {
          console.log('No se pudo obtener la ubicación:', error)
        }
      )
    }
  }

  const loadCategories = async () => {
    try {
      const response = await api.get('/categories/')
      setCategories(response.data.results || response.data)
    } catch (error) {
      console.error('Error loading categories:', error)
    }
  }

  const loadRoutes = async () => {
    setLoading(true)
    try {
      const params = new URLSearchParams()
      if (filters.search) params.append('search', filters.search)
      if (filters.category) params.append('category', filters.category)
      params.append('ordering', filters.ordering)
      params.append('page_size', '100') // Cargar hasta 100 lugares

      const response = await api.get(`/routes/?${params}`)
      setRoutes(response.data.results || response.data)
    } catch (error) {
      console.error('Error loading routes:', error)
    } finally {
      setLoading(false)
    }
  }

  const handleFilterChange = (key, value) => {
    const newFilters = { ...filters, [key]: value }
    setFilters(newFilters)
    
    const params = new URLSearchParams()
    if (newFilters.search) params.set('search', newFilters.search)
    if (newFilters.category) params.set('category', newFilters.category)
    setSearchParams(params)

    if (key === 'search' && value.length > 1) {
      const filtered = routes.filter(route => 
        route.name.toLowerCase().includes(value.toLowerCase()) ||
        route.description?.toLowerCase().includes(value.toLowerCase())
      ).slice(0, 5)
      setSuggestions(filtered)
      setShowSuggestions(true)
    } else {
      setShowSuggestions(false)
    }
  }

  const handleSuggestionClick = (routeName) => {
    handleFilterChange('search', routeName)
    setShowSuggestions(false)
  }

  const handleFavoriteToggle = (routeId) => {
    loadRoutes()
  }

  return (
    <div className="routes-page">
      <div className="routes-header">
        <div className="header-content">
          <div className="header-icon">
            <MapPin size={48} strokeWidth={1.5} />
          </div>
          <h1>Explora Lugares Increíbles</h1>
          <p>Descubre {routes.length}+ lugares verificados cerca de ti</p>
        </div>
      </div>

      <div className="routes-filters-container">
        <div className="filters-wrapper">
          <div className="filter-group search-group">
            <div className="search-wrapper">
              <Search className="filter-icon" size={20} />
              <input
                type="text"
                placeholder="Buscar lugares, restaurantes, museos..."
                value={filters.search}
                onChange={(e) => handleFilterChange('search', e.target.value)}
                onFocus={() => filters.search.length > 1 && setShowSuggestions(true)}
                onBlur={() => setTimeout(() => setShowSuggestions(false), 200)}
                className="search-input"
              />
              {filters.search && (
                <X 
                  className="clear-search" 
                  size={18} 
                  onClick={() => handleFilterChange('search', '')}
                />
              )}
              {showSuggestions && suggestions.length > 0 && (
                <div className="suggestions-dropdown">
                  {suggestions.map((suggestion) => (
                    <div
                      key={suggestion.id}
                      className="suggestion-item"
                      onClick={() => handleSuggestionClick(suggestion.name)}
                    >
                      <MapPin size={16} />
                      <div className="suggestion-content">
                        <div className="suggestion-name">{suggestion.name}</div>
                        <div className="suggestion-category">{suggestion.category_name}</div>
                      </div>
                    </div>
                  ))}
                </div>
              )}
            </div>
          </div>

          <div className="filter-group">
            <Filter className="filter-icon" size={20} />
            <select
              value={filters.category}
              onChange={(e) => handleFilterChange('category', e.target.value)}
              className="filter-select"
            >
              <option value="">Todas las categorías</option>
              {categories.map((category) => (
                <option key={category.id} value={category.id}>
                  {category.icon} {category.name}
                </option>
              ))}
            </select>
          </div>

          <div className="filter-group">
            <Filter className="filter-icon" size={20} />
            <select
              value={filters.ordering}
              onChange={(e) => handleFilterChange('ordering', e.target.value)}
              className="filter-select"
            >
              <option value="-created_at">Más recientes</option>
              <option value="name">Nombre (A-Z)</option>
              <option value="-rating">Mejor calificación</option>
            </select>
          </div>

          <button 
            className={`btn-toggle-map ${showMap ? 'active' : ''}`}
            onClick={() => setShowMap(!showMap)}
          >
            {showMap ? (
              <>
                <List size={20} />
                <span>Vista Lista</span>
              </>
            ) : (
              <>
                <Map size={20} />
                <span>Ver Mapa</span>
              </>
            )}
          </button>
        </div>
        
        <div className="results-count">
          {loading ? 'Cargando...' : `${routes.length} lugares encontrados`}
        </div>
      </div>

      {userLocation && routes.length > 0 && (
        <NearbyPlaces routes={routes} userLocation={userLocation} />
      )}

      {showMap && routes.length > 0 && (
        <div className="map-container">
          <div className="map-info">
            <h3>📍 Mapa Interactivo</h3>
            <p>Tu ubicación se muestra en tiempo real. Los iconos representan diferentes categorías de lugares.</p>
          </div>
          <MapView routes={routes} showUserLocation={true} zoom={13} />
        </div>
      )}

      {loading ? (
        <div className="loading-container">
          <div className="loading-spinner"></div>
          <p>Cargando lugares increíbles...</p>
        </div>
      ) : routes.length === 0 ? (
        <div className="no-results">
          <Search className="no-results-icon" size={64} />
          <h3>No encontramos lugares</h3>
          <p>Intenta con otros filtros o búsqueda</p>
          <button 
            className="btn-reset-filters"
            onClick={() => {
              setFilters({ search: '', category: '', ordering: '-created_at' })
              setSearchParams({})
            }}
          >
            <X size={18} />
            Limpiar Filtros
          </button>
        </div>
      ) : (
        <div className="routes-grid">
          {routes.map((route) => (
            <RouteCard 
              key={route.id} 
              route={route}
              onFavoriteToggle={handleFavoriteToggle}
            />
          ))}
        </div>
      )}
    </div>
  )
}

export default Routes

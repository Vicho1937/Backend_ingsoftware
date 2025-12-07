import { useState, useEffect } from 'react'
import { MapPin, Navigation } from 'lucide-react'
import { Link } from 'react-router-dom'
import '../styles/NearbyPlaces.css'

function NearbyPlaces({ routes, userLocation }) {
  const [nearbyRoutes, setNearbyRoutes] = useState([])

  useEffect(() => {
    if (userLocation && routes.length > 0) {
      calculateNearbyRoutes()
    }
  }, [userLocation, routes])

  const calculateDistance = (lat1, lon1, lat2, lon2) => {
    const R = 6371 // Radio de la Tierra en km
    const dLat = (lat2 - lat1) * Math.PI / 180
    const dLon = (lon2 - lon1) * Math.PI / 180
    const a = 
      Math.sin(dLat/2) * Math.sin(dLat/2) +
      Math.cos(lat1 * Math.PI / 180) * Math.cos(lat2 * Math.PI / 180) *
      Math.sin(dLon/2) * Math.sin(dLon/2)
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a))
    return R * c
  }

  const calculateNearbyRoutes = () => {
    const routesWithDistance = routes
      .filter(route => route.latitude && route.longitude)
      .map(route => ({
        ...route,
        distance: calculateDistance(
          userLocation[0],
          userLocation[1],
          parseFloat(route.latitude),
          parseFloat(route.longitude)
        )
      }))
      .sort((a, b) => a.distance - b.distance)
      .slice(0, 5) // Top 5 lugares más cercanos

    setNearbyRoutes(routesWithDistance)
  }

  if (!userLocation || nearbyRoutes.length === 0) {
    return null
  }

  return (
    <div className="nearby-places">
      <div className="nearby-header">
        <MapPin size={24} />
        <h3>Lugares Cercanos a Ti</h3>
      </div>
      <p className="nearby-description">
        Basados en tu ubicación actual
      </p>
      <div className="nearby-list">
        {nearbyRoutes.map((route, index) => (
          <Link to={`/routes/${route.id}`} key={route.id} className="nearby-item">
            <div className="nearby-rank">#{index + 1}</div>
            <div className="nearby-icon">{route.category_icon || '📍'}</div>
            <div className="nearby-info">
              <h4>{route.name}</h4>
              <p className="nearby-category">{route.category_name}</p>
              <div className="nearby-meta">
                <span className="nearby-distance">
                  <Navigation size={14} />
                  {route.distance < 1 
                    ? `${Math.round(route.distance * 1000)}m` 
                    : `${route.distance.toFixed(1)}km`}
                </span>
                <span className="nearby-rating">
                  ⭐ {route.average_rating?.toFixed(1) || '0.0'}
                </span>
              </div>
            </div>
          </Link>
        ))}
      </div>
    </div>
  )
}

export default NearbyPlaces

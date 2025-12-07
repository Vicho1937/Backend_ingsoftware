import { MapContainer, TileLayer, Marker, Popup, useMap } from 'react-leaflet'
import { useEffect, useState } from 'react'
import 'leaflet/dist/leaflet.css'
import L from 'leaflet'
import { Link } from 'react-router-dom'

// Iconos personalizados por categoría
const categoryIcons = {
  'Restaurantes': '🍽️',
  'Cafeterías': '☕',
  'Bares': '🍺',
  'Museos': '🏛️',
  'Parques': '🌳',
  'Monumentos': '🗿',
  'Teatro': '🎭',
  'Cines': '🎬',
  'Tiendas': '🛍️',
  'Hoteles': '🏨',
  'Gimnasios': '💪',
  'Hospitales': '🏥',
  'Farmacias': '💊',
  'Bancos': '🏦',
  'Educación': '📚',
  'default': '📍'
}

// Crear iconos HTML personalizados para cada categoría
const createCustomIcon = (categoryName, emoji) => {
  const icon = emoji || categoryIcons[categoryName] || categoryIcons.default
  return L.divIcon({
    html: `<div style="font-size: 32px; text-align: center; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);">${icon}</div>`,
    className: 'custom-marker',
    iconSize: [40, 40],
    iconAnchor: [20, 40],
    popupAnchor: [0, -40]
  })
}

// Icono para la ubicación del usuario con avatar y círculo pulsante
const userLocationIcon = L.divIcon({
  html: `
    <div style="position: relative; width: 50px; height: 50px;">
      <div style="
        position: absolute;
        width: 50px;
        height: 50px;
        background: rgba(66, 133, 244, 0.3);
        border-radius: 50%;
        animation: pulseRing 2s infinite;
      "></div>
      <div style="
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        width: 24px;
        height: 24px;
        background: #4285F4;
        border: 3px solid white;
        border-radius: 50%;
        box-shadow: 0 2px 8px rgba(0,0,0,0.3);
        z-index: 2;
      ">
        <div style="
          position: absolute;
          top: 50%;
          left: 50%;
          transform: translate(-50%, -50%);
          font-size: 12px;
        ">👤</div>
      </div>
    </div>
  `,
  className: 'user-location-marker',
  iconSize: [50, 50],
  iconAnchor: [25, 25],
  popupAnchor: [0, -25]
})

// Componente para manejar la ubicación del usuario
function UserLocation({ setUserLocation }) {
  const map = useMap()

  useEffect(() => {
    if (navigator.geolocation) {
      const watchId = navigator.geolocation.watchPosition(
        (position) => {
          const userPos = [position.coords.latitude, position.coords.longitude]
          setUserLocation(userPos)
        },
        (error) => {
          console.error('Error obteniendo ubicación:', error)
        },
        {
          enableHighAccuracy: true,
          maximumAge: 10000,
          timeout: 5000
        }
      )

      return () => navigator.geolocation.clearWatch(watchId)
    }
  }, [map, setUserLocation])

  return null
}

function MapView({ routes, center = [-33.4489, -70.6693], zoom = 13, showUserLocation = true }) {
  const [userLocation, setUserLocation] = useState(null)

  return (
    <MapContainer 
      center={center} 
      zoom={zoom} 
      style={{ height: '500px', width: '100%', borderRadius: '12px', boxShadow: '0 4px 12px rgba(0,0,0,0.1)' }}
    >
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />
      
      {showUserLocation && <UserLocation setUserLocation={setUserLocation} />}
      
      {/* Marcador de ubicación del usuario */}
      {userLocation && (
        <Marker position={userLocation} icon={userLocationIcon}>
          <Popup>
            <div style={{ textAlign: 'center' }}>
              <strong>📍 Tu ubicación</strong>
              <br />
              <small>Ubicación en tiempo real</small>
            </div>
          </Popup>
        </Marker>
      )}
      
      {/* Marcadores de lugares con iconos personalizados */}
      {routes.map((route) => {
        if (route.latitude && route.longitude) {
          const icon = createCustomIcon(route.category_name, route.category_icon)
          return (
            <Marker 
              key={route.id} 
              position={[parseFloat(route.latitude), parseFloat(route.longitude)]}
              icon={icon}
            >
              <Popup>
                <div style={{ minWidth: '200px' }}>
                  <strong style={{ fontSize: '16px', color: '#d4af37' }}>{route.name}</strong>
                  <br />
                  <span style={{ fontSize: '14px', color: '#666' }}>{route.category_name}</span>
                  <br />
                  <span style={{ fontSize: '12px' }}>📍 {route.address}</span>
                  <br />
                  <span style={{ fontSize: '14px', fontWeight: 'bold' }}>⭐ {route.average_rating?.toFixed(1) || '0.0'}</span>
                  <br />
                  <Link 
                    to={`/routes/${route.id}`} 
                    style={{ 
                      display: 'inline-block', 
                      marginTop: '8px', 
                      padding: '6px 12px',
                      background: 'linear-gradient(135deg, #d4af37 0%, #ffd700 100%)',
                      color: '#0a0a0a',
                      textDecoration: 'none',
                      borderRadius: '6px',
                      fontWeight: 'bold',
                      fontSize: '12px'
                    }}
                  >
                    Ver detalles
                  </Link>
                </div>
              </Popup>
            </Marker>
          )
        }
        return null
      })}
    </MapContainer>
  )
}

export default MapView

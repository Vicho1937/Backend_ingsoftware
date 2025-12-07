import { useState, useRef, useEffect } from 'react'
import { Link, useNavigate, useLocation } from 'react-router-dom'
import { useAuth } from '../context/AuthContext'
import { Menu, Home, Map, MessageCircle, Heart, User, Settings, LogOut, X } from 'lucide-react'
import '../styles/Navbar.css'

function Navbar() {
  const { user, logout } = useAuth()
  const navigate = useNavigate()
  const location = useLocation()
  const [isSidebarOpen, setIsSidebarOpen] = useState(false)
  const [isUserMenuOpen, setIsUserMenuOpen] = useState(false)
  const userMenuRef = useRef(null)

  const handleLogout = async () => {
    await logout()
    setIsUserMenuOpen(false)
    navigate('/login')
  }

  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen)
  }

  const closeSidebar = () => {
    setIsSidebarOpen(false)
  }

  const toggleUserMenu = () => {
    setIsUserMenuOpen(!isUserMenuOpen)
  }

  // Cerrar menú de usuario al hacer click fuera
  useEffect(() => {
    const handleClickOutside = (event) => {
      if (userMenuRef.current && !userMenuRef.current.contains(event.target)) {
        setIsUserMenuOpen(false)
      }
    }

    if (isUserMenuOpen) {
      document.addEventListener('mousedown', handleClickOutside)
    }

    return () => {
      document.removeEventListener('mousedown', handleClickOutside)
    }
  }, [isUserMenuOpen])

  // Cerrar sidebar cuando cambia la ruta
  useEffect(() => {
    closeSidebar()
  }, [location])

  const menuItems = [
    { path: '/', icon: Home, label: 'Inicio' },
    { path: '/routes', icon: Map, label: 'Explorar' },
    { path: '/chat', icon: MessageCircle, label: 'Asistente' },
    { path: '/favorites', icon: Heart, label: 'Favoritos' },
  ]

  return (
    <>
      <nav className="navbar">
        <div className="navbar-container">
          {/* Sección Izquierda - Menú Hamburguesa */}
          <div className="navbar-left">
            <button 
              className="hamburger-button" 
              onClick={toggleSidebar}
              aria-label="Menú"
            >
              <Menu size={28} strokeWidth={2.5} />
            </button>
          </div>

          {/* Sección Centro - Logo o Título de Página */}
          {location.pathname === '/chat' ? (
            <div className="navbar-page-title">
              <span className="page-title-icon">🤖</span>
              <span className="page-title-text">Chatbot IA</span>
            </div>
          ) : (
            <Link to="/" className="navbar-logo">
              <span className="logo-icon">📍</span>
              <span className="logo-text">Ruta Local</span>
            </Link>
          )}

          {/* Sección Derecha - Usuario/Auth */}
          <div className="navbar-right">
            {/* Botón Salir del Chat (solo visible en /chat) */}
            {location.pathname === '/chat' && (
              <button 
                onClick={() => navigate('/')} 
                className="btn-exit-navbar"
                title="Salir del chat"
              >
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                  <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                  <polyline points="16 17 21 12 16 7" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                  <line x1="21" y1="12" x2="9" y2="12" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
                </svg>
                Salir
              </button>
            )}
            
            {user ? (
              <div className="user-menu-container" ref={userMenuRef}>
                <button 
                  className="user-button"
                  onClick={toggleUserMenu}
                >
                  <User size={20} />
                  <span className="user-name">{user.username}</span>
                </button>

                {/* Dropdown de Usuario */}
                {isUserMenuOpen && (
                  <div className="user-dropdown">
                    <Link 
                      to="/profile" 
                      className="dropdown-item"
                      onClick={() => setIsUserMenuOpen(false)}
                    >
                      <Settings size={18} />
                      <span>Editar Perfil</span>
                    </Link>
                    <button 
                      className="dropdown-item logout"
                      onClick={handleLogout}
                    >
                      <LogOut size={18} />
                      <span>Cerrar Sesión</span>
                    </button>
                  </div>
                )}
              </div>
            ) : (
              <div className="auth-buttons">
                <Link to="/login" className="btn-auth btn-login">
                  Iniciar Sesión
                </Link>
                <Link to="/register" className="btn-auth btn-register">
                  Registrarse
                </Link>
              </div>
            )}
          </div>
        </div>
      </nav>

      {/* Overlay del Sidebar */}
      {isSidebarOpen && (
        <div className="sidebar-overlay" onClick={closeSidebar}></div>
      )}

      {/* Sidebar Menú */}
      <aside className={`sidebar ${isSidebarOpen ? 'open' : ''}`}>
        <div className="sidebar-header">
          <h2>Menú</h2>
          <button 
            className="sidebar-close"
            onClick={closeSidebar}
            aria-label="Cerrar menú"
          >
            <X size={24} />
          </button>
        </div>

        <nav className="sidebar-nav">
          {menuItems.map((item) => (
            <Link
              key={item.path}
              to={item.path}
              className={`sidebar-item ${location.pathname === item.path ? 'active' : ''}`}
              onClick={closeSidebar}
            >
              <item.icon size={22} />
              <span>{item.label}</span>
            </Link>
          ))}
        </nav>

        {/* Footer del Sidebar */}
        <div className="sidebar-footer">
          <div className="sidebar-user-info">
            {user ? (
              <>
                <User size={20} />
                <span>{user.username}</span>
              </>
            ) : (
              <span className="sidebar-guest">Visitante</span>
            )}
          </div>
        </div>
      </aside>
    </>
  )
}

export default Navbar

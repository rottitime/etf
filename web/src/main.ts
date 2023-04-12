import './style/vars.css'
import './style/animation.css'
import './style/base.css'
import './style/buttons.css'
import './style/template/index.css'
import './style/template/main-header.css'
import './style/forms/index.css'
import './style/forms/checkbox.css'
import './style/forms/radio.css'
import './style/components/index.css'
import './style/components/breadcrumb.css'
import './style/components/card.css'
import './style/components/menu-list.css'
import './style/components/accordion.css'
import './style/pages.css'
import accordion from './components/accordion'
import setupCard from './components/card'
import icon from './components/icon'
import setupSelect from './components/dropdown'
import setupFilters from './components/filters'
import setupSmoothScroll from './components/smooth-scroll'
import setupMobileMenu, { cleanup as mobileMenuCleanup } from './components/mobile-menu'

//local development purposes only. to replace prod assets with dev
declare global {
  function myFunction(): boolean
  // eslint-disable-next-line no-var
  var devMode: boolean
}

if (import.meta.env.MODE === 'development') {
  globalThis.devMode = true
  ;['main-script', 'main-css'].forEach((id) => document.getElementById(id)?.remove())
}

window.addEventListener('load', () => {
  if (globalThis.devMode && import.meta.env.MODE === 'production') return

  accordion()
  setupCard()
  icon()
  setupSelect()
  setupFilters()
  setupSmoothScroll()
  setupMobileMenu()
})

window.addEventListener('DOMContentLoaded', () => {
  const isTablet = window.matchMedia('(min-width: 800px)')

  const onViewportChange = () => {
    if (isTablet.matches) {
      mobileMenuCleanup()
    }
  }

  isTablet.addEventListener('change', onViewportChange)
})

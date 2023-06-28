import './style/vars.css'
import './style/animation.css'
import './style/fonts.css'
import './style/base.css'
import './style/template/index.css'
import './style/template/main-header.css'
import './style/forms/index.css'
import './style/forms/form-group.css'
import './style/forms/checkbox.css'
import './style/forms/radio.css'
import './style/forms/select.css'
import './style/forms/multiselect.css'
import './style/components/index.css'
import './style/components/accordion.css'
import './style/components/alert.css'
import './style/components/buttons.css'
import './style/components/breadcrumb.css'
import './style/components/card.css'
import './style/components/chip.css'
import './style/components/datagrid.css'
import './style/components/hintbox.css'
import './style/components/menu-list.css'
import './style/components/phase-banner.css'
import './style/components/progress-list.css'
import './style/components/filters-accordion.css'
import './style/components/circular-progress-bar.css'
import './style/pages.css'
import './style/components/progress-bar-horizontal.css'
import './style/components/progress-bar-horizontal-wide.css'
import './style/utilities.css'
import setupFiltersAccordion from './components/filters-accordion'
import setupAccordion from './components/accordion'
import setupCard from './components/card'
import icon from './components/icon'
import setupSelect from './components/dropdown'
import setupFilters from './components/filters'
import setupSmoothScroll from './components/smooth-scroll'
import setupMobileMenu, { cleanup as mobileMenuCleanup } from './components/mobile-menu'
import setupHintbox from './components/hintbox'
import setupMultiselect from './components/multiselect'
import setupCircularProgressBar from './components/circular-progress-bar'
import { fixNumberMaxLength } from './components/utils'

//local development purposes only. to replace prod assets with dev
declare global {
  function myFunction(): boolean
  // eslint-disable-next-line no-var
  var devMode: boolean
}

//check if dev scripts have executed when in prod mode
const hasDevScripts = (): boolean =>
  globalThis.devMode && globalThis.devMode && import.meta.env.MODE !== 'development'

//high priority scripts
;(function () {
  if (hasDevScripts()) return
  icon()
  setupHintbox()
  setupSelect()
  setupMultiselect()
  setupAccordion()
})()

//low priority scripts
window.addEventListener('load', () => {
  //check: dev mode has already been set then do not run prod files
  if (hasDevScripts()) return
  setupFiltersAccordion()
  setupCard()
  setupFilters()
  setupSmoothScroll()
  setupMobileMenu()
  setupCircularProgressBar()
  fixNumberMaxLength()
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

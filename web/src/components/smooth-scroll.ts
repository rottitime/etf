import { scrollToElement } from './utils'

const setupSmoothScroll = () => {
  document.querySelectorAll<HTMLAnchorElement>('a.smooth-scroll').forEach((el) => {
    el.addEventListener('click', (e) => {
      e.preventDefault()
      const href = (e.target as HTMLAnchorElement)?.getAttribute('href')
      const scollElement = href && document.querySelector<HTMLElement>(href)

      !!scollElement && scrollToElement(scollElement, false, 16)
    })
  })
}

export default setupSmoothScroll

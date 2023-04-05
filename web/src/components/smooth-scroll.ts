import { scrollToElement } from './utils'

const setupSmoothScroll = () => {
  document.querySelectorAll<HTMLAnchorElement>('a.smooth-scroll').forEach((el) => {
    el.addEventListener('click', (e) => {
      e.preventDefault()
      const href = (e.target as HTMLAnchorElement)?.getAttribute('href')
      const scrollElement = href && document.querySelector<HTMLElement>(href)

      if (scrollElement) {
        scrollElement.classList.remove('scrolled')
        scrollElement.classList.add('scrolling')
        scrollToElement(scrollElement, true, 16, () => {
          scrollElement.classList.remove('scrolling')
          scrollElement.classList.add('scrolled')
        })
      }
    })
  })
}

export default setupSmoothScroll

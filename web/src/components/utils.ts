//funciton to slugify a string
export const slugify = (str: string) => {
  return str
    .toLowerCase()
    .replace(/ /g, '-')
    .replace(/[^\w-]+/g, '')
}

export function scrollToElement(
  element: HTMLElement,
  onlyIfNotVisibleInView = false,
  buffer = 0,
  callback?: () => void
): void {
  const rect = element.getBoundingClientRect()

  // If the onlyIfNotVisibleInView flag is set, only scroll if the element is not visible in the view
  if (onlyIfNotVisibleInView && rect.top >= 0 && rect.bottom <= window.innerHeight) {
    callback && callback()
    return
  }

  if (callback) {
    let lastScrollPos = window.pageYOffset
    let isScrolling = false

    const checkScroll = () => {
      if (window.pageYOffset === lastScrollPos) {
        isScrolling = false
        callback()
      } else {
        lastScrollPos = window.pageYOffset
        requestAnimationFrame(checkScroll)
      }
    }

    const onScrollComplete = () => {
      if (!isScrolling) {
        isScrolling = true
        requestAnimationFrame(checkScroll)
      }
    }

    window.addEventListener('scroll', onScrollComplete)
  }

  window.scrollTo({
    top: rect.top + window.pageYOffset - buffer,
    behavior: 'smooth'
  })
}

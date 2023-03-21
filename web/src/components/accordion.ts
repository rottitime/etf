import iconRaw from '../svg/arrow-down.svg'
import shortUUID from 'short-uuid'

const setupAccordions = () => {
  const removeAllActive = (el: Element) => {
    el.parentNode
      ?.querySelectorAll('.active')
      .forEach((active) => active.classList.remove('active'))
  }

  //icons
  document.querySelectorAll('.accordion .icon').forEach((icon) => {
    icon.insertAdjacentHTML('beforeend', iconRaw)
  })

  //create wrapper
  document.querySelectorAll('.accordion-content').forEach((content) => {
    const id = `wrapper-${shortUUID.generate()}`
    const buttonid = `button-${shortUUID.generate()}`
    const wrapper = document.createElement('div')
    const parent = content.parentNode
    const parentButton = parent?.querySelector('button')

    wrapper.classList.add('accordion-content-wrapper')
    wrapper.setAttribute('id', id)
    wrapper.setAttribute('role', 'region')
    wrapper.setAttribute('aria-labelledby', buttonid)

    wrapper?.addEventListener('transitionend', () => wrapper.setAttribute('style', ''))
    parent?.insertBefore(wrapper, content)
    parentButton?.setAttribute('aria-controls', id)
    parentButton?.setAttribute('id', buttonid)
    parentButton?.setAttribute(
      'aria-expanded',
      new Boolean(parentButton?.classList.contains('active')).toString()
    )

    wrapper.appendChild(content)
  })

  //click behaviour
  document.querySelectorAll('.accordion li').forEach((accordion) => {
    const wrapper = accordion.querySelector(
      '.accordion-content-wrapper'
    ) as HTMLDivElement
    const content = wrapper?.querySelector('.accordion-content')

    accordion.querySelector('button')?.addEventListener('click', (e) => {
      const el = e?.target as HTMLButtonElement
      const parent = el?.parentNode as Element

      if (parent?.classList.contains('active')) {
        removeAllActive(accordion)
        el.setAttribute('aria-expanded', 'false')
      } else {
        const height = content?.clientHeight
        removeAllActive(accordion)
        parent.classList.add('active')
        wrapper?.setAttribute('style', `max-height:${height}px`)
        el.setAttribute('aria-expanded', 'true')
      }
    })
  })
}

export default setupAccordions

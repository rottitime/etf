import shortUUID from 'short-uuid'

// This function adds a click event listener to each card element that contains an accordion.
// It also adds an aria-expanded attribute to the header element of each card with an accordion.
// The aria-expanded attribute is set to true if the accordion is initially open, and false otherwise.
// When the header is clicked, the aria-expanded attribute is toggled between true and false.

const setupCards = () => {
  document.querySelectorAll<HTMLDivElement>('.card.with-accordion').forEach((card) => {
    const header = card.querySelector('header')
    const content = card.querySelector('.content')
    const id = shortUUID.generate()
    const contentId = `content-${id}`
    const buttonId = `button-${id}`
    const open = true

    if (!header || !content) return

    header.setAttribute('role', 'button')
    header.setAttribute('aria-expanded', Boolean(open).toString())
    header.setAttribute('aria-controls', contentId)
    header.setAttribute('id', buttonId)
    header.setAttribute('aria-controls', Boolean(open).toString())

    content.setAttribute('id', contentId)
    content.setAttribute('aria-labelledby', buttonId)
    content.setAttribute('role', 'region')

    header.addEventListener('click', () => {
      const opened = header.getAttribute('aria-expanded') === 'true'
      header.setAttribute('aria-expanded', String(!opened))
    })
  })
}

export default setupCards

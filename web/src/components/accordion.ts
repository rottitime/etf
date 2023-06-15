class Accordion extends HTMLDivElement {
  constructor() {
    super()
  }

  connectedCallback() {
    setTimeout(() => this.setup())
  }

  private setupButtons() {
    this.querySelectorAll('.accordion-title').forEach((button) => {
      button.setAttribute('role', 'button')
    })
  }

  private createShowAll() {
    const button = document.createElement('button')
    button.setAttribute('type', 'button')
    button.setAttribute('class', 'show-all')
    button.setAttribute('aria-expanded', 'false')
    button.innerText = 'Show all sections'
    return button
  }

  private setup() {
    this.setupButtons()
    const showAll = this.createShowAll()

    this.prepend(showAll)
  }
}

const setupAccordion = () =>
  customElements.define('idotai-accordion', Accordion, { extends: 'div' })

export default setupAccordion

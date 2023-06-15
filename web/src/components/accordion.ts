class Accordion extends HTMLDivElement {
  buttonId: string
  sectionId: string

  constructor() {
    super()

    const id = crypto.randomUUID()
    this.buttonId = `btn-${id}`
    this.sectionId = `pnl-${id}`
  }

  connectedCallback() {
    setTimeout(() => this.setup())
  }

  private setupPanels() {
    this.querySelectorAll('.accordion-panel').forEach((panel, i) => {
      panel.setAttribute('role', 'region')
      panel.setAttribute('aria-labelledby', this.buttonId + `-${i}`)
      panel.id = this.sectionId + `-${i}`
    })
  }

  private setupButtons() {
    this.querySelectorAll('.accordion-title').forEach((button, i) => {
      button.setAttribute('role', 'button')
      button.id = this.buttonId + `-${i}`
      button.setAttribute(
        'aria-expanded',
        String(button.getAttribute('aria-expanded') === 'true' || false)
      )
      button.setAttribute('aria-controls', this.sectionId + `-${i}`)

      //event to toggle aria-expanded
      button.addEventListener('click', () => {
        const expanded = button.getAttribute('aria-expanded') === 'true' || false
        button.setAttribute('aria-expanded', String(!expanded))
      })
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
    this.setupPanels()
    const showAll = this.createShowAll()

    this.prepend(showAll)
  }
}

const setupAccordion = () =>
  customElements.define('idotai-accordion', Accordion, { extends: 'div' })

export default setupAccordion

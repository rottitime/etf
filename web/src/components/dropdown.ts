class SelectField extends HTMLDivElement {
  constructor() {
    super()
  }

  connectedCallback() {
    this.setup()
  }

  private setup() {
    const select = this.querySelector('select') as HTMLSelectElement

    this.setHasValue(select)
    select.addEventListener('change', (e) =>
      this.setHasValue(e.target as HTMLSelectElement)
    )
  }

  private setHasValue = (target: HTMLSelectElement) => {
    const parent = target?.parentNode as HTMLDivElement
    const { value } = target
    const classname = 'has-value'

    return value ? parent?.classList.add(classname) : parent?.classList.remove(classname)
  }
}

const setupSelect = () =>
  customElements.define('select-field', SelectField, { extends: 'div' })

export default setupSelect

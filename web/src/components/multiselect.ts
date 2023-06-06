class MultiSelect extends HTMLDivElement {
  constructor() {
    super()
  }

  connectedCallback() {
    this.setup()
  }

  private populateTags() {
    const options = this.querySelector('select')?.selectedOptions

    console.log('options', { options })
    const values = options ? Array.from(options).map(({ value }) => value) : []

    const selectedValues = this.querySelector('.selected-values') as HTMLDivElement
    selectedValues.innerHTML = ''

    values.forEach((value) => {
      const tag = document.createElement('div')
      tag.classList.add('chip')
      tag.innerHTML = value

      const icon = document.createElement('gov-icon')
      icon.classList.add('close')
      icon.setAttribute('key', 'cross')
      icon.setAttribute('role', 'button')

      tag.appendChild(icon)

      selectedValues?.appendChild(tag)
    })
  }

  private toggleOption(value: HTMLSelectElement) {
    value.selected = !value.selected
    // value.focus()
    // const multiselect = this.querySelector('select')
    // const options = multiselect?.querySelectorAll('option')
    // const option = Array.from(options || []).find((option) => option.value === value)
    // if (options) {
    //   const isSelected = options[0].selected
    //   console.log('option', { option, isSelected })
    //   options[1].selected = !isSelected
    // }
    // option?.setAttribute('selected', option.selected ? 'false' : 'true')
  }

  private setup() {
    const selectedValues = document.createElement('div')
    selectedValues.classList.add('selected-values')
    this.prepend(selectedValues)

    const multiselect = this.querySelector('select')

    this.populateTags()
    multiselect?.addEventListener('change', () => this.populateTags())

    multiselect?.addEventListener('mousedown', (event) => {
      event.preventDefault()
      const option = event.target as HTMLSelectElement
      this.toggleOption(option)
      this.populateTags() //TODO: bug causes jumping
      // console.log('dedede', { event, value })
    })

    //   const id = crypto.randomUUID()
    //   const idContent = `content_${id}`
    //   const idButton = `button_${id}`
    //   const content = this.querySelector('.content')
    //   if (!content) return
    //   //button setup
    //   const toggleBtn = document.createElement('button')
    //   toggleBtn.setAttribute('id', idButton)
    //   toggleBtn.classList.add('txt-link')
    //   toggleBtn.setAttribute('type', 'button')
    //   toggleBtn.setAttribute('aria-expanded', this.dataset.open || 'false')
    //   toggleBtn.setAttribute('aria-controls', idContent)
    //   toggleBtn.innerHTML = help + (this.getAttribute('aria-label') || 'Hint')
    //   toggleBtn.addEventListener('click', () => {
    //     const opened = toggleBtn.getAttribute('aria-expanded') === 'true'
    //     toggleBtn.setAttribute('aria-expanded', String(!opened))
    //   })
    //   this.prepend(toggleBtn)
    //   //content wrapper
    //   const wrapper = document.createElement('div')
    //   const parent = content.parentNode
    //   wrapper.classList.add('content-wrapper')
    //   wrapper.setAttribute('id', idContent)
    //   wrapper.setAttribute('aria-labelledby', idButton)
    //   wrapper.setAttribute('role', 'region')
    //   parent?.insertBefore(wrapper, content)
    //   wrapper.appendChild(content)
    //   this.removeAttribute('hidden')
  }
}

const setupMultiselect = () =>
  customElements.define('multi-select', MultiSelect, { extends: 'div' })

export default setupMultiselect

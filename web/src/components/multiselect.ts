class MultiSelect extends HTMLDivElement {
  constructor() {
    super()
  }

  connectedCallback() {
    console.log('connected')
    this.setup()
    // this.setAttribute('hidden', 'true') //hide while rendering. prevents flash of unstyled content
    // setTimeout(() => this.setup())
  }

  private populateTags() {
    const options = this.querySelector('select')?.selectedOptions
    const values = options ? Array.from(options).map(({ value }) => value) : []

    const selectedValues = this.querySelector('.selected-values') as HTMLDivElement
    selectedValues.innerHTML = ''

    console.log(values)

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

    // values?.forEach((value) => {
    //   const tag = document.createElement('span')
    //   tag.classList.add('tag')
    //   tag.innerHTML = value.innerHTML
    //   selectedValues?.appendChild(tag)
    // })

    // debugger
  }

  private setup() {
    const selectedValues = document.createElement('div')
    selectedValues.classList.add('selected-values')
    this.prepend(selectedValues)

    const multiselect = this.querySelector('select')
    this.populateTags()

    multiselect?.addEventListener('change', () => {
      this.populateTags()
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

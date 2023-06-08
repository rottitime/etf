import '../style/filters.css'

const submit = (filterControl: HTMLElement, category?: string) => {
  const form = filterControl.closest('form') as HTMLFormElement

  if (form) {
    //set active filter
    form
      .querySelector<HTMLInputElement>('input[type="hidden"][name="active_filter"]')
      ?.setAttribute('value', category ? category : '')
    form.submit()
  }
}

const onReset = (filterControl: HTMLElement) => {
  filterControl.querySelectorAll('button[type="reset"]').forEach((button) => {
    button.addEventListener('click', () => {
      const checkboxes = filterControl.querySelectorAll<HTMLInputElement>(
        'input[type=checkbox][name]:checked'
      )

      checkboxes.forEach((checkbox) => {
        checkbox.removeAttribute('checked')
        checkbox.checked = false
      })

      submit(filterControl, checkboxes[0]?.name)
    })
  })
}

const setupSearch = (filterControl: HTMLElement) => {
  filterControl
    .querySelectorAll<HTMLInputElement>('input[data-controls]')
    .forEach((search) => {
      search.addEventListener('keyup', () => {
        const value = search.value.toLowerCase()
        const { controls } = search.dataset
        filterControl
          .querySelectorAll<HTMLInputElement>(
            `input[type=checkbox][name=${controls}][value]`
          )
          .forEach((checkbox) => {
            const parent = checkbox.closest<HTMLLabelElement>('.checkbox')
            if (parent) {
              parent?.textContent?.toLowerCase().includes(value)
                ? (parent.style.display = '')
                : (parent.style.display = 'none')
            }
          })
      })
    })
}

const onFilterClick = (filterControl: HTMLElement) => {
  // let checked = false
  filterControl
    .querySelectorAll<HTMLInputElement>('input[type="checkbox"]')
    .forEach((checkbox) => {
      // if (checkbox.checked) checked = true
      checkbox.addEventListener('change', () => {
        const { name } = checkbox

        submit(filterControl, name)
      })
    })
}

const setupFilters = () => {
  document.querySelectorAll<HTMLElement>('.filter-control').forEach((filterControl) => {
    onReset(filterControl)
    onFilterClick(filterControl)
    setupSearch(filterControl)
  })
}

export default setupFilters

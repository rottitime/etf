import '../style/filters.css'

const setTotal = (filterControl: HTMLElement, name: string) => {
  const total = filterControl.querySelectorAll(`[name=${name}]:checked`).length

  document
    .querySelectorAll(`.filter-control-total[data-name=${name}]`)
    .forEach((control) => {
      control.innerHTML = total.toString()
    })
}

const setupFilters = () => {
  document.querySelectorAll<HTMLElement>('.filter-control').forEach((filterControl) => {
    filterControl.querySelectorAll('button[type="reset"]').forEach((button) => {
      button.addEventListener('click', () => {
        const checkboxes = filterControl.querySelectorAll<HTMLInputElement>(
          'input[type=checkbox][name]:checked'
        )

        checkboxes.forEach((checkbox) => {
          checkbox.removeAttribute('checked')
          checkbox.checked = false
        })

        !!checkboxes.length && setTotal(filterControl, checkboxes[0].name)
      })
    })
  })

  document
    .querySelectorAll('.filter-control input[type="checkbox"]')
    .forEach((checkbox) => {
      checkbox.addEventListener('change', (e) => {
        const checkbox = e.target as HTMLInputElement
        const { name } = checkbox
        const parent = checkbox.closest('.filter-control') as HTMLElement
        setTotal(parent, name)
      })
    })
}

export default setupFilters

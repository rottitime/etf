import '../style/filters.css'

const submit = (filterControl: HTMLElement) => {
  const form = filterControl.closest('form')
  !!form && form.submit()
}

// const setTotal = (filterControl: HTMLElement, name: string) => {
// const total = filterControl.querySelectorAll(`[name=${name}]:checked`).length
// const reset = filterControl.querySelector('button[type="reset"]')
// if (reset)
//   total ? reset.removeAttribute('disabled') : reset.setAttribute('disabled', 'true')
// document
//   .querySelectorAll(`.filter-control-total[data-name=${name}]`)
//   .forEach((control) => {
//     control.innerHTML = total.toString()
//   })
// }

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

      // !!checkboxes.length && setTotal(filterControl, checkboxes[0].name)

      submit(filterControl)
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
        // const checkbox = e.target as HTMLInputElement
        // const { name } = checkbox
        // setTotal(filterControl, name)
        submit(filterControl)
      })
    })

  // if (!checked)
  //   filterControl.querySelector('button[type="reset"]')?.setAttribute('disabled', 'true')
}

const setupFilters = () => {
  document.querySelectorAll<HTMLElement>('.filter-control').forEach((filterControl) => {
    onReset(filterControl)
    onFilterClick(filterControl)
  })
}

export default setupFilters

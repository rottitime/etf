import '../style/filters.css'

const setTotal = (filterControl: HTMLElement, name: string) => {
  const total = filterControl.querySelectorAll(`[name=${name}]:checked`).length

  console.log({ total, name })

  document
    .querySelectorAll(`.filter-control-total[data-name=${name}]`)
    .forEach((control) => {
      console.log({ control })
      control.innerHTML = total.toString()
    })
}

const setupFilters = () => {
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

const setHasValue = (target: HTMLSelectElement) => {
  const parent = target?.parentNode as HTMLDivElement
  const { value } = target
  const classname = 'has-value'

  return value ? parent?.classList.add(classname) : parent?.classList.remove(classname)
}

const setupSelect = () => {
  document.querySelectorAll('.select select').forEach((select) => {
    setHasValue(select)
    select.addEventListener('change', (e) => setHasValue(e.target as HTMLSelectElement))
  })
}

export default setupSelect

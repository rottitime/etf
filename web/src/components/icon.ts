const setupIcons = () => {
  const prefix = 'icon-'
  document.querySelectorAll(`i[class^="${prefix}"]`).forEach(async (e) => {
    const iconName = e.className.replace(prefix, '')
    const html = await import(`../svg/${iconName}.svg?ddede`)
    e.outerHTML = html.default
  })
}

export default setupIcons

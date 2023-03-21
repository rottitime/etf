const setupIcons = () => {
  const prefix = 'icon-'

  document.querySelectorAll(`i[class^="${prefix}"]`).forEach(async (e) => {
    const iconName = e.className.replace(prefix, '')

    const html = await import(`../svg/${iconName}.svg`)

    console.log(iconName, e, html)

    // e.replaceChild(module.default)
    e.outerHTML = html.default

    // currentNode.parentNode.replaceChild(newNode, currentNode);
  })
}

export default setupIcons

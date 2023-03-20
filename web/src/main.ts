import './style/vars.css'
import './style/base.css'
import './style/template.css'
import './style/forms.css'
import './style/components.css'

//local development purposes only. to replace prod assets with dev
if (import.meta.env.MODE === 'development') {
  ;['main-script', 'main-css'].forEach((id) => document.getElementById(id)?.remove())
}

const initAccordions = () => {
  const accordionItems = document.querySelectorAll('.accordion li')

  //remove all active classname
  const removeAllActive = (el: Element) => {
    el.parentNode
      ?.querySelectorAll('.active')
      .forEach((active) => active.classList.remove('active'))
  }

  //create wrapper
  document.querySelectorAll('.accordion-content').forEach((content) => {
    const wrapper = document.createElement('div')
    wrapper.classList.add('accordion-content-wrapper')
    wrapper?.addEventListener('transitionend', () => wrapper.setAttribute('style', ''))
    content.parentNode?.insertBefore(wrapper, content)
    wrapper.appendChild(content)
  })

  //click behaviour
  accordionItems.forEach((accordion) => {
    const button = accordion.querySelector('button')
    const wrapper = accordion.querySelector(
      '.accordion-content-wrapper'
    ) as HTMLDivElement
    const content = wrapper?.querySelector('.accordion-content')

    button?.addEventListener('click', () => {
      if (button.classList.contains('active')) {
        removeAllActive(accordion)
      } else {
        const height = content?.clientHeight
        removeAllActive(accordion)
        button.classList.add('active')
        wrapper?.setAttribute('style', `max-height:${height}px`)
      }
    })
  })
}

window.addEventListener('load', () => {
  initAccordions()
})

// import typescriptLogo from './typescript.svg'
// import viteLogo from '/vite.svg'
// import { setupCounter } from './counter'

// document.querySelector<HTMLDivElement>('#app')!.innerHTML = `
//   <div>
//     <a href="https://vitejs.dev" target="_blank">
//       <img src="${viteLogo}" class="logo" alt="Vite logo" />
//     </a>
//     <a href="https://www.typescriptlang.org/" target="_blank">
//       <img src="${typescriptLogo}" class="logo vanilla" alt="TypeScript logo" />
//     </a>
//     <h1>Vite + TypeScript</h1>
//     <div class="card">
//       <button id="counter" type="button"></button>
//     </div>
//     <p class="read-the-docs">
//       Click on the Vite and TypeScript logos to learn more
//     </p>
//   </div>
// `

// setupCounter(document.querySelector<HTMLButtonElement>('#counter')!)

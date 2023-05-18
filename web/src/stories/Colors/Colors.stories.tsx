const palette = [
  '--color-white',
  '--color-green',
  '--color-green-light',
  '--color-purple',
  '--color-pink',
  '--color-orange',
  '--color-blue',
  '--color-blue2',
  '--color-blue-light',
  '--color-blue-light2',
  '--color-red',
  '--color-black',
  '--color-grey-dark',
  '--color-grey-light',
  '--color-grey-light2'
]

const meta = {
  title: 'ETF/Colors',
  tags: ['autodocs'],
  render: () =>
    `<div class="color-wrapper">${palette.map(
      (color) =>
        `<div class="color-block" style="background-color:var(${color})">${color}</div>`
    )}</div>`,
  parameters: {
    design: {
      type: 'figma',
      url: 'https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=1-386&t=NMzWF77GnAa7BvPp-0'
    }
  }
}

export default meta

export const Palette = {}

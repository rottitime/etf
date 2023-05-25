import type { StoryObj, Meta } from '@storybook/html'
import { action } from '@storybook/addon-actions'

type Props = {
  title: string
  content: string
  actions: boolean
  onClick: () => void
}

/**
 * A banner to indicate the current phase of the service.
 */
const meta = {
  title: 'Components/Card',
  tags: ['autodocs'],
  render: ({ title, content, actions, onClick }) => {
    const card = document.createElement('div')
    card.classList.add('card')

    const header = document.createElement('header')
    const p = document.createElement('p')
    p.textContent = content

    const h1 = document.createElement('h1')
    h1.textContent = title
    h1.classList.add('header2', 'highlight')
    header.append(h1)
    card.append(header)

    card.append(p)

    if (actions) {
      const footer = document.createElement('footer')
      footer.classList.add('actions')
      const btnPrimary = document.createElement('button')
      btnPrimary.classList.add('bttn-primary', 'primary-action')
      btnPrimary.setAttribute('type', 'submit')
      btnPrimary.textContent = 'Save'
      btnPrimary.addEventListener('click', onClick)

      const div = document.createElement('div')
      const btnCancel = document.createElement('a')
      btnCancel.classList.add('bttn-quaternary', 'small')
      btnCancel.setAttribute('href', '#')
      btnCancel.textContent = 'Cancel'
      btnCancel.addEventListener('click', onClick)

      btnCancel.addEventListener('click', () => {
        action('Link Clicked')()
      })

      const btnDelete = document.createElement('button')
      btnDelete.classList.add('bttn-negative', 'small')
      btnDelete.setAttribute('type', 'submit')
      btnDelete.textContent = 'Delete'
      btnDelete.addEventListener('click', onClick)
      div.append(btnCancel)
      div.append(btnDelete)
      footer.append(btnPrimary)
      footer.append(div)
      card.append(footer)
    }

    return card
  },
  argTypes: {
    title: { control: 'text' },
    content: { control: 'text' },
    actions: { control: 'boolean', table: { disable: true } },
    onClick: { action: 'clicked', table: { disable: true } }
  },
  parameters: {
    backgrounds: {
      default: 'light grey'
    },
    design: {
      type: 'figma',
      url: 'https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=481-545&t=FJwPXpig0RTCQXW7-0'
    }
  }
} satisfies Meta<Props>

export default meta
type Story = StoryObj<Props>

export const Default: Story = {
  args: {
    title: 'Card component',
    content:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed rutrum mollis eros, at luctus ligula tincidunt eget. Maecenas lacus diam, dapibus id condimentum a, congue venenatis neque. Aenean lobortis molestie risus, sit amet vehicula tellus iaculis maximus. Nulla eros orci, interdum sed est in, lobortis eleifend erat. Vivamus et dictum risus. Phasellus gravida pharetra lectus, sed varius lectus posuere ac. Integer molestie purus quis quam imperdiet tincidunt.'
  }
}

export const WithButtons: Story = {
  args: {
    ...Default.args,
    actions: true
  }
}

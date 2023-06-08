import type { StoryObj, Meta } from '@storybook/html'
import { createCard, Card as Props } from './utils'
import setupCards from '../components/card'

const meta = {
  title: 'Components/Card',
  tags: ['autodocs'],
  render: (p) => createCard(p).outerHTML,
  argTypes: {
    title: { control: 'text' },
    content: { control: 'text' },
    actions: { control: 'boolean', table: { disable: true } },
    small: { control: 'boolean' },
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
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed rutrum mollis eros, at luctus ligula tincidunt eget. Maecenas lacus diam, dapibus id condimentum a, congue venenatis neque. Aenean lobortis molestie risus, sit amet vehicula tellus iaculis maximus. Nulla eros orci, interdum sed est in, lobortis eleifend erat. Vivamus et dictum risus. Phasellus gravida pharetra lectus, sed varius lectus posuere ac. Integer molestie purus quis quam imperdiet tincidunt.',
    small: false
  }
}

export const WithButtons: Story = {
  args: {
    ...Default.args,
    actions: true
  }
}

export const WithAccordion: Story = {
  args: {
    ...Default.args,
    accordion: true,
    open: true
  },
  //reload the accordion setup for cards
  loaders: [
    async () => {
      return setTimeout(() => Promise.resolve(setupCards()))
    }
  ]
}

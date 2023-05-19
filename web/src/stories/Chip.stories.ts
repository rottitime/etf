import type { StoryObj, Meta } from '@storybook/html'

enum Color {
  Pink = '',
  Purple = 'purple',
  Green = 'green',
  Orange = 'orange'
}

type Props = {
  color?: keyof typeof Color
  hasClose?: boolean
  label: string
}

/**
 * A divider to separate content.
 */
const meta = {
  title: 'Components/Chip',
  tags: ['autodocs'],
  render: ({ color, label, hasClose }) => {
    const chip = document.createElement('div')
    chip.classList.add('chip')
    chip.innerText = label
    if (color) chip.classList.add(color)

    if (hasClose) {
      const close = document.createElement('a')
      close.setAttribute('title', 'close')
      close.classList.add('close')
      close.innerHTML = '<gov-icon key="cross"></gov-icon>'
      chip.appendChild(close)
    }

    return chip
  },
  argTypes: {
    label: { control: 'text' },
    hasClose: { control: 'boolean', table: { disable: true } },
    color: {
      control: { type: 'select' },
      options: Color
    }
  },
  parameters: {
    design: {
      type: 'figma',
      url: 'https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=38-107&t=5eFOsFvCi3xiEsBW-0'
    }
  }
} satisfies Meta<Props>

export default meta
type Story = StoryObj<Props>

export const Default: Story = {
  args: {
    label: 'My chip'
  }
}

export const WithClose: Story = {
  args: {
    ...Default.args,
    hasClose: true
  }
}

import type { StoryObj, Meta } from '@storybook/html'

enum Color {
  Default = '',
  Green = 'green',
  Orange = 'orange',
  Red = 'red',
  Blue = 'blue'
}

type Props = {
  color?: keyof typeof Color
  label: string
}

/**
 * A divider to separate content.
 */
const meta = {
  title: 'Components/Status',
  tags: ['autodocs'],
  render: ({ color, label }) => {
    const chip = document.createElement('div')
    chip.classList.add('chip')
    chip.setAttribute('role', 'status')
    chip.innerText = label
    if (color) chip.classList.add(color.toLowerCase())
    return chip
  },
  argTypes: {
    label: { control: 'text' },
    color: {
      control: { type: 'select' },
      options: Color
    }
  },
  parameters: {
    design: {
      type: 'figma',
      url: 'https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=30-100&t=5eFOsFvCi3xiEsBW-0'
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

export const Green: Story = {
  args: {
    ...Default.args,
    color: 'Green'
  }
}

export const Orange: Story = {
  args: {
    ...Default.args,
    color: 'Orange'
  }
}

export const Red: Story = {
  args: {
    ...Default.args,
    color: 'Red'
  }
}

export const Blue: Story = {
  args: {
    ...Default.args,
    color: 'Blue'
  }
}

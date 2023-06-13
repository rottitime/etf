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
/**
 * ##When to use this component
Use the chip component when it’s possible for something to have more than one status and it’s useful for the user to know about that status. For example, you can use a chip to show whether an item in a task list has been ‘completed’.
 * 
*##How it works

Chips are used solely for indicating the status of an item, and so links should not be added to them. When naming your chips, it's recommended to use adjectives instead of verbs. The use of verbs may lead a user to believe that clicking on a chip will perform an action.
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

export const WithClose: Story = {
  args: {
    ...Default.args,
    hasClose: true
  }
}

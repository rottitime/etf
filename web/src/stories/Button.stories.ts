import type { StoryObj, Meta } from '@storybook/html'
import { createButton, Button } from './utils'

// More on how to set up stories at: https://storybook.js.org/docs/html/writing-stories/introduction#default-export
const meta = {
  title: 'Components/Button',
  tags: ['autodocs'],
  render: (args) => {
    // You can either use a function to create DOM elements or use a plain html string!
    // return `<div>${label}</div>`;
    return createButton(args)
  },
  argTypes: {
    label: { control: 'text' },
    onClick: {
      action: 'onClick',
      table: {
        disable: true
      }
    },
    small: { control: 'boolean' }
  },
  parameters: {
    design: {
      type: 'figma',
      url: 'https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=1-388&t=wYAx110qILxbxZUz-0'
    }
  }
} satisfies Meta<Button>

export default meta
type Story = StoryObj<Button>

// More on writing stories with args: https://storybook.js.org/docs/html/writing-stories/args
export const Primary: Story = {
  args: {
    label: 'Button'
  }
}

export const Secondary: Story = {
  args: {
    ...Primary.args,
    category: 'secondary'
  }
}

export const Tertiary: Story = {
  args: {
    ...Primary.args,
    category: 'tertiary'
  }
}

export const Negative: Story = {
  args: {
    ...Primary.args,
    category: 'negative'
  }
}

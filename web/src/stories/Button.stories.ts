import type { StoryObj, Meta } from '@storybook/html'
import { createButton, Button } from './utils'
/**
 * Use the button component to help users carry out an action like starting an application or saving their information.
 * ## When to use this component
 * Services must use the phase banner until they pass a live assessment.
 * Use an alpha banner when your service is in alpha, and a beta banner if your service is in private or public beta.
 *
 * ##How it works
 * Button text should be written in sentence case and describe the action it performs. For instance:



*  ##Primary buttons
* On a page, ensure that the main call to action is represented by a primary button. It is not recommended to have multiple primary buttons on a single page, as having more than one main call to action can lessen their effectiveness. This can confuse users and make it difficult for them to determine what action to take next.
 *
 * 
 */
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

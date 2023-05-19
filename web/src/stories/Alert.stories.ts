import type { StoryObj, Meta } from '@storybook/html'

enum Status {
  Success,
  Error,
  Warning
}

type Props = {
  status?: keyof typeof Status
  text: string
}

/**
 * A banner to indicate the current phase of the service.
 */
const meta = {
  title: 'Components/Alert',
  tags: ['autodocs'],
  render: ({ text, status }) =>
    `<div class="alert ${status?.toLowerCase()}">${text}</div>`,
  argTypes: {
    text: { control: 'text' },
    status: {
      control: { type: 'select' },
      options: Object.values(Status).filter((v) => isNaN(Number(v)))
    }
  },
  parameters: {
    design: {
      type: 'figma',
      url: 'https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=488-791&t=5eFOsFvCi3xiEsBW-0'
    }
  }
} satisfies Meta<Props>

export default meta
type Story = StoryObj<Props>

export const Success: Story = {
  args: {
    text: 'This is an error alert — check it out!',
    status: 'Success'
  }
}

export const Error: Story = {
  args: {
    ...Success.args,
    status: 'Error'
  }
}

export const Warning: Story = {
  args: {
    ...Success.args,
    status: 'Warning'
  }
}

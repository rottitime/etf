import type { StoryObj, Meta } from '@storybook/html'

type Props = {
  content: string
}

/**
 * A badge to indicate the current phase of the service.
 */
const meta = {
  title: 'Components/Badge',
  tags: ['autodocs'],
  render: ({ content }) => `<span class="badge">${content}</span>`,
  argTypes: {
    content: { control: 'text' }
  },
  parameters: {
    design: {
      type: 'figma',
      url: 'https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=53-451&t=VoS0cvSv4a0gcPEO-0'
    }
  }
} satisfies Meta<Props>

export default meta
type Story = StoryObj<Props>

export const Badge: Story = {
  args: {
    content: '1'
  }
}

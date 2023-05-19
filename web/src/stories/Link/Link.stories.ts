import type { StoryObj, Meta } from '@storybook/html'

type Props = {
  text: string
  external?: boolean
}

/**
 * A banner to indicate the current phase of the service.
 */
const meta = {
  title: 'Components/Link',
  tags: ['autodocs'],
  render: ({ text, external }) =>
    `<a href="#" class="txt-link"${external ? ' rel="external"' : ''}>${text}</a>`,
  argTypes: {
    text: { control: 'text' },
    external: { control: 'boolean' }
  },
  parameters: {
    design: {
      type: 'figma',
      url: 'https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=1-273&t=FJwPXpig0RTCQXW7-0'
    }
  }
} satisfies Meta<Props>

export default meta
type Story = StoryObj<Props>

export const Link: Story = {
  args: {
    text: 'My link'
  }
}

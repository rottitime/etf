import type { StoryObj, Meta } from '@storybook/html'

type Props = {
  label: string
  content: string
}

/**
 * A banner to indicate the current phase of the service.
 */
const meta = {
  title: 'Components/Hintbox',
  tags: ['autodocs'],
  render: ({ label, content }) =>
    `<hint-box aria-label="${label}">
    <div class="content">
        <p>${content}</p>
    </div>
  </hint-box>`,
  argTypes: {
    label: { control: 'text' },
    content: { control: 'text' }
  },
  parameters: {
    design: {
      type: 'figma',
      url: 'https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=320-429&t=ur05zeF7bSVeJzta-0'
    }
  }
} satisfies Meta<Props>

export default meta
type Story = StoryObj<Props>

export const Hintbox: Story = {
  args: {
    label: 'Additional guidance',
    content:
      'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis consectetur mollis dignissim. Vestibulum facilisis pulvinar quam vitae mollis. Duis fermentum ut tellus vel interdum.'
  }
}

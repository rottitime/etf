import type { StoryObj, Meta } from '@storybook/html'

type Props = {
  tag: string
  text: string
}

/**
 * A banner to indicate the current phase of the service.
 */
const meta = {
  title: 'Components/Phase Banner',
  tags: ['autodocs'],
  render: ({ tag, text }) =>
    `<div class="phase-banner">
    <div class="container">            
     <p>
       <strong class="tag">${tag}</strong>
       <span>${text}</span>
    </p>
    </div>
 </div>`,
  argTypes: {
    tag: { control: 'text' },
    text: { control: 'text' }
  },
  parameters: {
    backgrounds: {
      default: 'light grey'
    },
    design: {
      type: 'figma',
      url: 'https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=488-948&t=NMzWF77GnAa7BvPp-0'
    }
  }
} satisfies Meta<Props>

export default meta
type Story = StoryObj<Props>

export const PhaseBanner: Story = {
  args: {
    tag: 'ALPHA',
    text: 'This is a new service - your feedback will help us to improve it.'
  }
}

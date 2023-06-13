import type { StoryObj, Meta } from '@storybook/html'

type Props = {
  tag: string
  text: string
}

/**
 * A banner to indicate the current phase of the service.
 * ## When to use this component
 * Services must use the phase banner until they pass a live assessment.
 * Use an alpha banner when your service is in alpha, and a beta banner if your service is in private or public beta.
 *
 * ##How it works
 * Your banner must be directly under the black GOV.UK header and colour bar.
 * 
 * ##Add a feedback link
 * Use a ‘feedback’ link to collect on-page feedback about your service. This can open an email or take the user to a dedicated page or form. Whatever option you use, make sure that users do not lose their place in the service and can return to the page they were on.
 * 
 * 
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
    tag: {
      control: 'text',
      name: 'Tag text',
      description: 'The tag to display in the banner e.g. ALPHA, BETA'
    },
    text: { control: 'text', name: 'Content', description: 'Banner content' }
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

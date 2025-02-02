import type { StoryObj, Meta } from '@storybook/html'
import { createInput, Input as Props } from '../utils'
/** The date input component helps users enter a memorable date or one they can easily look up. 
 * ##When to use this component
 * Use the date input component when you’re asking users for a date they’ll already know, or can look up without using a calendar.
 * 
 * ##When not to use this component
 * Do not use the date input component if users are unlikely to know the exact date of the event you’re asking about.
 * 
 * 
 * 
*/
const meta = {
  title: 'Components/Form/Date Picker',
  tags: ['autodocs'],
  render: (props) => {
    const datePicker = document.createElement('div')
    datePicker.classList.add('date-picker')
    datePicker.appendChild(createInput(props))
    return datePicker
  },
  argTypes: {
    fullWidth: { control: 'boolean' },
    value: { control: 'text' },
    onkeyup: { action: 'changed', table: { disable: true } },
    type: { control: 'text', defaultValue: 'date', table: { disable: true } },
    dimension: {
      control: { type: 'select' },
      options: ['small', 'medium', 'large']
    }
  },
  parameters: {
    design: {
      type: 'figma',
      url: 'https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=27-75&t=ur05zeF7bSVeJzta-0'
    }
  }
} satisfies Meta<Props>

export default meta
type Story = StoryObj<Props>

export const DatePicker: Story = {
  args: {
    type: 'date',
    dimension: 'medium'
  }
}

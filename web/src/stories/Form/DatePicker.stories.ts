import type { StoryObj, Meta } from '@storybook/html'
import { createInput, Input as Props } from '../utils'

const meta = {
  title: 'Components/Form/DatePicker',
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
    type: { control: 'text', defaultValue: 'date', table: { disable: true } }
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
    type: 'date'
  }
}

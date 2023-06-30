import type { StoryObj, Meta } from '@storybook/html'

type Props = { otherLabel: string }

const meta = {
  title: 'Components/Form/Checkbox/Other',
  render: ({ otherLabel }) =>
    `<div class="form-group">
   <label class="checkbox">
     <input type="checkbox" name="measure_type" value="CONTINUOUS">
     <span class="checkmark"></span>
     <span>Continuous</span>
   </label>
   <label class="checkbox">
     <input type="checkbox" name="measure_type" value="DISCRETE">
     <span class="checkmark"></span>
     <span>Discrete</span>
   </label>
   <label class="checkbox">
     <input type="checkbox" name="measure_type" value="BINARY">
     <span class="checkmark"></span>
     <span>Binary</span>
   </label>
   <label class="checkbox">
     <input type="checkbox" name="measure_type" value="ORDINAL">
     <span class="checkmark"></span>
     <span>Ordinal</span>
   </label>
   <label class="checkbox">
     <input type="checkbox" name="measure_type" value="NOMINAL">
     <span class="checkmark"></span>
     <span>Nominal</span>      
   </label>
   <label class="checkbox">
     <input type="checkbox" name="measure_type" value="OTHER" aria-controls="conditional-dyt6y3i">
     <span class="checkmark"></span>
     <span>Other</span>
   </label>
   <div class="form-group controller-subfield" id="conditional-dyt6y3i">
     <label for="measure_type_other">${otherLabel}</label>
     <textarea placeholder="" id="measure_type_other" name="measure_type_other" class="full-width"></textarea>
   </div>
 </div>`,
  argTypes: {
    otherLabel: {
      control: 'text',
      description: 'Label for the other text input',
      name: 'Other label'
    }
  },
  parameters: {
    design: {
      type: 'figma',
      url: 'https://www.figma.com/file/pN3VtobnXOlTUDK4aiZa94/i-AI-DS?type=design&node-id=32-159&t=s7R0duWzGfG8Vf2S-0'
    }
  }
} satisfies Meta<Props>

export default meta
type Story = StoryObj<Props>

export const Other: Story = {
  args: {
    otherLabel: 'Please provide more detail'
  }
}

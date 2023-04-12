type Segment = {
  color: string
  percentage: number
}

function validSegments(segments: unknown): segments is Segment[] {
  if (!Array.isArray(segments)) return false

  return segments.every((segment) => {
    return (
      typeof segment === 'object' &&
      typeof segment.color === 'string' &&
      typeof segment.percentage === 'number' &&
      segment.percentage >= 0 &&
      segment.percentage <= 100
    )
  })
}

function createCircularProgressBar(container: HTMLElement, segments: Segment[]): void {
  const svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg')
  svg.setAttribute('viewBox', '0 0 100 100')
  svg.classList.add('progress-bar')

  const backgroundCircle = document.createElementNS(
    'http://www.w3.org/2000/svg',
    'circle'
  )
  backgroundCircle.setAttribute('cx', '50')
  backgroundCircle.setAttribute('cy', '50')
  backgroundCircle.setAttribute('r', '40')
  backgroundCircle.classList.add('progress-bar-background')

  svg.appendChild(backgroundCircle)

  const totalPercentage = segments.reduce((acc, segment) => acc + segment.percentage, 0)
  let totalProgress = 0

  segments.forEach((segment, index) => {
    let startingRotation = -90 - (totalPercentage / 2) * 1.5 - (1 / 6) * 360

    const progressCircle = document.createElementNS(
      'http://www.w3.org/2000/svg',
      'circle'
    )
    progressCircle.setAttribute('cx', '50')
    progressCircle.setAttribute('cy', '50')
    progressCircle.setAttribute('r', '40')
    progressCircle.classList.add('progress-bar-foreground')
    progressCircle.style.stroke = segment.color
    progressCircle.style.strokeDasharray = '0'
    progressCircle.style.strokeDashoffset = '0'
    progressCircle.style.transformOrigin = '50% 50%'
    progressCircle.style.transform = `rotate(${
      (totalProgress * 360) / 100 + startingRotation
    }deg)` // Updated rotation calculation

    svg.appendChild(progressCircle)

    const radius = progressCircle.getAttribute('r')
    if (typeof radius === 'string') {
      const numRadius = parseFloat(radius)
      const circumference = 2 * Math.PI * numRadius
      const dashOffset = circumference * (1 - segment.percentage / 100)

      progressCircle.style.strokeDasharray = `${circumference} ${circumference}`
      progressCircle.style.strokeDashoffset = dashOffset.toString()
    } else {
      console.error(
        'Failed to retrieve the radius attribute from the progressCircle element'
      )
    }

    totalProgress += segment.percentage
  })

  const purpleLine = document.createElementNS('http://www.w3.org/2000/svg', 'rect')
  purpleLine.setAttribute('x', '50')
  purpleLine.setAttribute('y', '11')
  purpleLine.setAttribute('width', '2')
  purpleLine.setAttribute('height', '25')
  purpleLine.style.fill = 'var(--color-purple)'
  purpleLine.style.transformOrigin = '50% 50%'
  purpleLine.style.transform = 'rotate(160deg) translateY(-14%)'

  svg.appendChild(purpleLine)

  container.appendChild(svg)
}

const setupCircularProgressBar = () => {
  const progressBarContainers = document.querySelectorAll('.circular-progress-bar')

  progressBarContainers.forEach((container: Element) => {
    try {
      const segmentsData = JSON.parse(container.getAttribute('data-segments') || 'null')

      if (validSegments(segmentsData)) {
        createCircularProgressBar(container as HTMLElement, segmentsData)
      } else {
        console.error(
          'Invalid data-segments attribute:',
          container.getAttribute('data-segments')
        )
      }
    } catch (error) {
      if (error instanceof Error) {
        console.error('Failed to parse data-segments:', error.message)
      } else {
        console.error('Failed to parse data-segments:', error)
      }
    }
  })
}

export default setupCircularProgressBar

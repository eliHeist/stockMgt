const URLS_OBJ = JSON.parse(localStorage.getItem('mbf-urls') as string)

declare const stock_create_page: boolean
declare const innerHtml: string

// updating a customer's details
async function customerUpdate(customer: object, csrf: string): Promise<Object> {
    const response = await fetch(URLS_OBJ.customers, {
        method: 'PUT',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf,
        },
        body: JSON.stringify(customer),
    })
    return await response.json();
}

// add new customer
async function customerCreate(customer: object, csrf: string): Promise<Object> {
    const response = await fetch(URLS_OBJ.customers, {
        method: 'POST',
        headers: {
            Accept: 'application/json',
            'Content-Type': 'application/json',
            'X-CSRFToken': csrf,
        },
        body: JSON.stringify(customer),
    })
    return await response.json();
}

async function GETFunc(url: string): Promise<object> {
    console.log(`url: ${url}`);
    const response = await fetch(url, { method: 'GET' })
    let data = await response.json();
    console.log(data);
    return data
}

if (stock_create_page) {
    let batch_index: number;
    const initialFormsInput = document.getElementById('id_batches-INITIAL_FORMS') as HTMLInputElement;

    if (initialFormsInput) {
        const initialValue = parseInt(initialFormsInput.value, 10);
        batch_index = initialValue + 1;
    } else {
        // Fallback value if the input element is not found
        batch_index = 1;
    }

    console.log(batch_index);

    document.addEventListener('DOMContentLoaded', function () {
        let addBatchBtn: Element | null = document.querySelector('#add-batch-btn')
        let batchFormset: Element | null = document.querySelector('#batch-formset')
        const totalFormsInput = document.getElementById('id_batches-TOTAL_FORMS') as HTMLInputElement;

        // adding a batch
        addBatchBtn?.addEventListener('click', () => {
            let batchForm: HTMLDivElement = document.createElement('div')
            batchForm.classList.add('batch-form')
            batchForm.classList.add('grid')
            batchForm.classList.add('border')
            batchForm.classList.add('p-4')
            batchForm.innerHTML = innerHtml.replace(/__prefix__/g, batch_index.toString())
            batch_index++
            console.log(batchForm);
            batchFormset?.appendChild(batchForm)
            // increment the total forms count
            if (totalFormsInput) {
                const currentValue = parseInt(totalFormsInput.value, 10);
                totalFormsInput.value = (currentValue + 1).toString();
            }

        })

        // delete a batch
        batchFormset?.addEventListener('click', (event: any) => {
            if (event.target && event.target.parentNode.classList.contains('delete-batch-btn')) {
                let batchForm = event.target.parentNode.parentNode;
                batchForm.remove()
                // decrement the total forms count
                if (totalFormsInput) {
                    const currentValue = parseInt(totalFormsInput.value, 10);
                    totalFormsInput.value = (currentValue - 1).toString();
                }
            }
        })
    })
}
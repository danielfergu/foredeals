import http from 'k6/http';
import { sleep, check } from 'k6';

function generateRandomEmail() {
    const randomString = Math.random().toString(36).substring(7);
    return `user_${randomString}@example.com`;
}

export const options = {
    vus: 1,
    duration: '1m',
};

export default function () {
    for (let i = 0; i < 1000; i++) {
        const dynamicData = {
            email: generateRandomEmail(),
            zip_code: Math.floor(Math.random() * 1000),
            sqft_price: Math.floor(Math.random() * 1000),
            min_sqft: Math.floor(Math.random() * 1000),
        };

        // Construct the URL with parameters
        const urlWithParams = `http://127.0.0.1:5000/notification?email=${dynamicData.email}&zip_code=${dynamicData.zip_code}&sqft_price=${dynamicData.sqft_price}&min_sqft=${dynamicData.min_sqft}`;

        // Make a GET request
        let res = http.get(urlWithParams);

        // Check for a 200 status code
        check(res, {
            'Status is 200': (r) => r.status === 200,
        });

        sleep(1);
    }
}

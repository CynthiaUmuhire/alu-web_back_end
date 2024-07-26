import { createQueue } from "kue";
import { createClient } from "redis";


const queue = createQueue({
    redis: {
        createClientFactory: () => createClient()
    }
});

const data = {
    phoneNumber: '0173943892',
    message: 'this is a message'
};

const job = queue.create('push_notification_code', data);



job.on('enqueue', () => {
    console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
    console.log(`Notification job completed`);
});

job.on('ailed attempt', () => {
    console.log('Notification job failed');
});

job.save()
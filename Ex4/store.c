// void non_preemptive(PriorityFunc pf, Event *event, double timedelta, double quanta) {
// 	handle_event_arrived_and_done(event, pf(event->pcb));

// 	if(event->type == QuantaOver) {
// 		cur_pcb->burst_left -= timedelta;
// 		pqueue_add(pqueue, init_pentry(cur_pcb->priority, cur_pcb), false);
// 		cur_pcb = NULL;
// 	}
		
// 	if(cur_pcb == NULL) {
// 		PEntry *entry = pqueue_extract_min(pqueue);
// 		if(entry != NULL) {
// 			cur_pcb = entry->pcb;
// 			if(cur_pcb->burst_left <= quanta) {
// 				event_queue_add(event_queue, init_event(event->time + cur_pcb->burst_left, cur_pcb, Done));
// 			} else {
// 				event_queue_add(event_queue, init_event(event->time + quanta, cur_pcb, QuantaOver));
// 			}
// 		}
// 		free(entry); 
// 	}
// }





// void sjfs_non_preemptive(Event *event, double timedelta) {

// 	handle_event_arrived_and_done(event, 1/event->pcb->burst_left);
		
// 	if(cur_pcb == NULL) {
// 		PEntry *entry = pqueue_extract_min(pqueue);
// 		if(entry != NULL) {
// 			cur_pcb = entry->pcb;
// 			event_queue_add(event_queue, init_event(event->time + cur_pcb->burst_left, cur_pcb, Done));
// 		}
// 		free(entry); 
// 	}
// }

// void round_robin_priority_nonpreemptive(Event *event, double timedelta, double quanta) {

// 	handle_event_arrived_and_done(event, event->pcb->priority);

// 	// if(event->type == Arrived) {
// 	// 	pqueue_add(pqueue, init_pentry(event->pcb->priority, event->pcb), false); 
// 	// }

// 	// if(event->type == Done) {
// 	// 	free(cur_pcb);
// 	// 	cur_pcb = NULL;
// 	// }

// 	if(event->type == QuantaOver) {
// 		cur_pcb->burst_left -= timedelta;
// 		pqueue_add(pqueue, init_pentry(cur_pcb->priority, cur_pcb), false);
// 		cur_pcb = NULL;
// 	}
		
// 	if(cur_pcb == NULL) {
// 		PEntry *entry = pqueue_extract_min(pqueue);
// 		if(entry != NULL) {
// 			cur_pcb = entry->pcb;
// 			if(cur_pcb->burst_left <= quanta) {
// 				event_queue_add(event_queue, init_event(event->time + cur_pcb->burst_left, cur_pcb, Done));
// 			} else {
// 				event_queue_add(event_queue, init_event(event->time + quanta, cur_pcb, QuantaOver));
// 			}
// 		}
// 		free(entry); 
// 	}
// }

// void preemptive(PriorityFunc pf, Event *event, double timedelta) {
// 	handle_event_arrived_and_done(event, pf(event->pcb));

// 	if(cur_pcb != NULL) {
// 		event_queue_remove(event_queue, cur_pcb->pid);
// 		cur_pcb->burst_left -= timedelta; 
// 		pqueue_add(pqueue, init_pentry(pf(cur_pcb), cur_pcb), true);
// 	}

// 	cur_pcb = NULL;
// 	PEntry *entry = pqueue_extract_min(pqueue);
// 	if(entry != NULL) {
// 		cur_pcb = entry->pcb;
// 		event_queue_add(event_queue, init_event(event->time + cur_pcb->burst_left, cur_pcb, Done));
// 	}
// 	free(entry);
// }

// void sjfs_preemptive(Event *event, double timedelta) {
// 	// if(event->type == Arrived) {
// 	// 	pqueue_add(pqueue, init_pentry(1/event->pcb->burst_left, event->pcb), false); 
// 	// }

// 	// if(event->type == Done) {
// 	// 	free(cur_pcb);
// 	// 	cur_pcb = NULL;
// 	// }

// 	handle_event_arrived_and_done(event, 1/event->pcb->burst_left);

// 	if(cur_pcb != NULL) {
// 		event_queue_remove(event_queue, cur_pcb->pid);
// 		cur_pcb->burst_left -= timedelta; 
// 		pqueue_add(pqueue, init_pentry(1/cur_pcb->burst_left, cur_pcb), true);
// 	}

// 	cur_pcb = NULL;
// 	PEntry *entry = pqueue_extract_min(pqueue);
// 	if(entry != NULL) {
// 		cur_pcb = entry->pcb;
// 		event_queue_add(event_queue, init_event(event->time + cur_pcb->burst_left, cur_pcb, Done));
// 	}
// 	free(entry); 
// }


// void priority_preemptive(Event *event, double timedelta) {
// 	// if(event->type == Arrived) {
// 	// 	pqueue_add(pqueue, init_pentry(event->pcb->priority, event->pcb), false); 
// 	// }

// 	// if(event->type == Done) {
// 	// 	free(cur_pcb);
// 	// 	cur_pcb = NULL;
// 	// }

// 	handle_event_arrived_and_done(event, event->pcb->priority);

// 	if(cur_pcb != NULL) {
// 		event_queue_remove(event_queue, cur_pcb->pid);
// 		cur_pcb->burst_left -= timedelta; 
// 		pqueue_add(pqueue, init_pentry(cur_pcb->priority, cur_pcb), true);
// 	}

// 	cur_pcb = NULL;
// 	PEntry *entry = pqueue_extract_min(pqueue);
// 	if(entry != NULL) {
// 		cur_pcb = entry->pcb;
// 		event_queue_add(event_queue, init_event(event->time + cur_pcb->burst_left, cur_pcb, Done));
// 	}

// 	free(entry); 
// }

// void handle_event_arrived_and_done(Event *event, double priority) {
// 	if(event->type == Arrived) {
// 		pqueue_add(pqueue, init_pentry(priority, event->pcb), false); 
// 	}

// 	if(event->type == Done) {
// 		free(cur_pcb);
// 		cur_pcb = NULL;
// 	}
// }

// void fcfs_priority_non_preemptive(Event *event) {
// 	if(event->type == Arrived) {
// 		pqueue_add(pqueue, init_pentry(event->pcb->priority, event->pcb), false); 
// 	}

// 	if(event->type == Done) {
// 		free(cur_pcb)
// 		cur_pcb = NULL;		
// 	}
		
// 	if(cur_pcb == NULL) {
// 		PEntry *entry = pqueue_extract_min(pqueue);
// 		if(entry != NULL) {
// 			cur_pcb = entry->pcb;
// 			event_queue_add(event_queue, init_event(event->time + cur_pcb->burst_left, cur_pcb, Done));
// 		}
// 		free(entry); 
// 	}
// }
import React, { useState, useEffect, useRef } from 'react';
import { useWebSocket } from '../services/websocket';

const ChatbotUI = () => {
	const [messages, setMessages] = useState([]);
	const [input, setInput] = useState('');
	const messageContainerRef = useRef(null);
	const webSocketService = useWebSocket();

	useEffect(() => {
		let currentMessage = '';

		const handleMessage = (word) => {
			currentMessage += ` ${word}`;

			if (currentMessage.endsWith('\n')) {
				const completeMessage = currentMessage.trim();
				setMessages((prevMessages) => [
					...prevMessages,
					{ id: prevMessages.length + 1, text: completeMessage, sender: 'bot' },
				]);
				currentMessage = '';
			} else {
				// Update the last message in the messages array with the current word
				setMessages((prevMessages) => {
					const lastMessage = prevMessages[prevMessages.length - 1];
					if (lastMessage && lastMessage.sender === 'bot') {
						return [
							...prevMessages.slice(0, -1),
							{ ...lastMessage, text: lastMessage.text + ` ${word}` },
						];
					} else {
						return [
							...prevMessages,
							{ id: prevMessages.length + 1, text: word, sender: 'bot' },
						];
					}
				});
			}
		};

		webSocketService.addListener(handleMessage);

		return () => {
			webSocketService.removeListener(handleMessage);
		};
	}, [webSocketService, setMessages]);

	useEffect(() => {
		if (messageContainerRef.current) {
			messageContainerRef.current.scrollTop =
				messageContainerRef.current.scrollHeight;
		}
	}, [messages]);

	const sendMessage = () => {
		if (input.trim()) {
			const newMessage = {
				id: messages.length + 1,
				text: input,
				sender: 'user',
			};
			setMessages((prevMessages) => [...prevMessages, newMessage]);

			// Send the message to the server via WebSocket
			webSocketService.sendMessage(input);

			setInput('');

			// Scroll to the bottom of the chat window
			setTimeout(() => {
				if (messageContainerRef.current) {
					messageContainerRef.current.scrollTop =
						messageContainerRef.current.scrollHeight;
				}
			}, 0);
		}
	};

	return (
		<div className='chatbot-ui'>
			<div className='chat-window' ref={messageContainerRef}>
				{messages.map((msg) => (
					<div key={msg.id} className={`message ${msg.sender}`}>
						{msg.text}
					</div>
				))}
			</div>
			<div className='input-container'>
				<input
					value={input}
					onChange={(e) => setInput(e.target.value)}
					onKeyPress={(e) => e.key === 'Enter' && sendMessage()}
					placeholder='Type your message...'
				/>
				<button onClick={sendMessage}>Send</button>
			</div>
		</div>
	);
};

export default ChatbotUI;

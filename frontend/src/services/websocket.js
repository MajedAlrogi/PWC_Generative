import { useContext, useEffect, createContext } from 'react';

class WebSocketService {
	constructor() {
		this.socket = null;
		this.listeners = [];
	}

	connect(url) {
		this.socket = new WebSocket(url);

		this.socket.onopen = () => {
			console.log('WebSocket connection established');
		};

		this.socket.onmessage = (event) => {
			this.listeners.forEach((listener) => listener(event.data));
		};

		this.socket.onclose = () => {
			console.log('WebSocket connection closed');
		};
	}

	sendMessage(message) {
		if (this.socket && this.socket.readyState === WebSocket.OPEN) {
			this.socket.send(message);
		}
	}

	addListener(listener) {
		this.listeners.push(listener);
	}

	removeListener(listener) {
		this.listeners = this.listeners.filter((l) => l !== listener);
	}
}

const webSocketService = new WebSocketService();
const WebSocketContext = createContext(webSocketService);

export const WebSocketProvider = ({ children }) => {
	useEffect(() => {
		webSocketService.connect('ws://localhost:8000/ws');
	}, []);

	return (
		<WebSocketContext.Provider value={webSocketService}>
			{children}
		</WebSocketContext.Provider>
	);
};

export const useWebSocket = () => useContext(WebSocketContext);

export default webSocketService;

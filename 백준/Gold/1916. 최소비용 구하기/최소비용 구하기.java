
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.PriorityQueue;
import java.util.StringTokenizer;
/*
인접리스트로 구현을 했기때문에 static 인접리스트 list를 만들었고
갈 수 없는 경로인 INF를 만듬

다익스트라 알고리즘은 BFS와 굉장히 비슷하다
Queue가 빌때까지 반복하는 방식이다.
차이점이라면 다익스트라는 우선순위 큐인 PriorityQueue를 사용한다는 점이다.

그리고 처음 문제에서 나온대로 시작점인 start부터 갈 수 있는 모든곳의 최단 값을 출력하는 문제이기 때문에 전체를 탐색한다.

자기자신은 갈 수 없음은 아니지만 비용이 없으므로 dist[start]의 값을 0으로 해준다

이제 start부터 시작해서 갈 수 있는 모든 노드를 순회하며
que에 집어넣는는다.

check를 통해 각 노드를 방문했는지 하지 않았는지를 검사하고,
방문한적이 없는 노드를 우선으로 가중치 값을 계속 갱신하면서, 반복하면 답을 얻을 수 있다.
 */
public class Main {

	private static final int INF = Integer.MAX_VALUE / 16;
	static List<ArrayList<Node>> list;
	static int dist[];

	static int N;

	static class Node implements Comparable<Node> {
		int nodeNum;
		int weight;

		public Node(int nodeNum, int weight) {
			this.nodeNum = nodeNum;
			this.weight = weight;
		}

		@Override
		public int compareTo(Node o) {
			return weight - o.weight;
		}
	} // End of Node

	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;

		N = Integer.parseInt(br.readLine()); // 도시의 개수
		int M = Integer.parseInt(br.readLine()); // 버스의 개수
		

		list = new ArrayList<>();
		dist = new int[N + 1];
		Arrays.fill(dist, INF);

		for(int i=0; i<=N; i++) {
			list.add(new ArrayList<>());
		}
		
		for(int i=0; i<M; i++) {
			st = new StringTokenizer(br.readLine());

			int s = Integer.parseInt(st.nextToken());
			int d = Integer.parseInt(st.nextToken());
			int w = Integer.parseInt(st.nextToken());

			
			list.get(s).add(new Node(d, w));
		}
		
		st = new StringTokenizer(br.readLine());
		
		int start = Integer.parseInt(st.nextToken());
		int destination = Integer.parseInt(st.nextToken());
			
		System.out.println(dijkstra(start, destination));

	} // End of main

	static int dijkstra(int start, int destination) {
		PriorityQueue<Node> que = new PriorityQueue<Node>();
		boolean visit[] = new boolean[N + 1];

		dist[start] = 0;
		que.offer(new Node(start, 0));
		
		while( !que.isEmpty() ) {
			Node queNode = que.poll();
			int start_nodeNum = queNode.nodeNum;
			
			if( !visit[start_nodeNum] ) {
				visit[start_nodeNum] = true;
				
				for(Node node : list.get(start_nodeNum)) {
					
					if( !visit[node.nodeNum] && dist[node.nodeNum] > (dist[start_nodeNum] + node.weight) ) {
						dist[node.nodeNum] = dist[start_nodeNum] + node.weight;
						que.offer(new Node(node.nodeNum, dist[node.nodeNum]));
					}
				}
			}
		}
		
		return dist[destination];
	}

}
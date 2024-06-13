function minMovesToSeat(seats: number[], students: number[]): number {
    seats.sort((a,b))
    students.sort()
    let moves: number = 0
    for (let i = 0; i < seats.length; i++) {
         moves += Math.abs(seats[i] - students[i])
    }
    return moves
};

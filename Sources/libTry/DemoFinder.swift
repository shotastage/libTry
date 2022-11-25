//
//  DemoFinder.swift
//
//
//  Created by Shota Shimazu on 2022/07/10.
//

import Foundation


open class DemoFinder {

    let directoryIdentifier = [
        "*Example",
        "Examples",
        "*Sample",
        "*TestApp",
        "*Demo",
    ]

    func find() {
        for identifer in directoryIdentifier {
            print(identifer)
        }
    }
}
